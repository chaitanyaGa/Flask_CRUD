from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_httpauth import HTTPBasicAuth
from bson import ObjectId
from pymongo.errors import PyMongoError

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['jsonDatabase']
collection = db['jsonData']
auth = HTTPBasicAuth()

users = {
    "admin1": "admin1",
    "admin2": "admin2"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
@app.route('/data', methods=['POST'])
@auth.login_required
def create_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        result = collection.insert_one(data)
        return jsonify(str(result.inserted_id))
    except PyMongoError as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

@app.route('/data/<id>', methods=['GET'])
@auth.login_required
def get_data(id):
    try:
        data = collection.find_one({'_id': ObjectId(id)})
        if data:
            data['_id'] = str(data['_id'])  # Convert ObjectId to string
            return jsonify(data)
        else:
            return jsonify({'error': 'Data not found'}), 404
    except PyMongoError as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

@app.route('/data_all', methods=['GET'])
@auth.login_required
def get_all_data():
    try:
        data = collection.find()
        if data:
            result = []
            for d in data:
                d['_id'] = str(d['_id'])  # Convert ObjectId to string
                result.append(d)
            return jsonify(result)
        else:
            return jsonify({'error': 'Data not found'}), 404
    except PyMongoError as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

@app.route('/data/<id>', methods=['PUT'])
@auth.login_required
def update_data(id):
    try:
        updated_data = request.get_json()
        if not updated_data:
            return (jsonify({'error': 'Invalid JSON'}), 400)
        result = collection.update_one({'_id': ObjectId(id)},
                {'$set': updated_data})
        if result.modified_count == 0:
            return (jsonify({'error': 'Data not found'}), 404)
        else:
            return jsonify({'message': 'Data updated successfully'})
    except PyMongoError as e:
        return (jsonify({'error': f'Database error: {str(e)}'}), 500)

@app.route('/data/<id>', methods=['DELETE'])
@auth.login_required
def delete_data(id):
    try:
        result = collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Data not found'}), 404
        else:
            return jsonify({'message': 'Data deleted successfully'})
    except PyMongoError as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the home page'})
   
if __name__ == '__main__':
    app.run(debug=True)
