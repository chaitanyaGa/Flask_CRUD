# Flask CRUD
Basic application for Demo purpose for use of Flask and MongoDB for  CRUD operations

This is Python Flask application establishes a RESTful API to perform CRUD operations on a MongoDB database. The added error handling includes:
1. Verification of valid JSON data for POST and PUT requests
2. Handling MongoDB connection errors using PyMongoError exceptions
3. Returning appropriate error responses for missing data, invalid JSON, and database connection issues
	
Also It is containerized using Dockerfile.

The API also incorporates basic authentication using flask_httpauth. This ensures that only authorized users with valid credentials can perform updates.

By including robust error handling, the API becomes more reliable and can effectively communicate error with end client application/GUI, improving the overall user experience.

REST Verbs implemented:

* POST     --> to store record in DB. <br />
             ```
             curl -X POST -H "Content-Type: application/json" -u admin1:admin1 -d '{"key": "Value", .....}' http://localhost:5000/data
             ```
* GET      --> To retrieve single or multiple records from mongoDB database.<br />
              ```
              curl -X GET -H "Content-Type: application/json" -u admin1:admin1 http://localhost:5000/data/<id>                             
              curl -X GET -H "Content-Type: application/json" -u admin1:admin1 http://localhost:5000/data_all 
              ```
* PUT      --> To update single Database record <br />
               ```
               curl -X PUT -H "Content-Type: application/json" -u admin1:admin1 -d '{"key": "Value"}' http://localhost:5000/data/<id>
               ```
* DELETE   --> to Delete the record <br />
              ```
               curl -X DELETE-H "Content-Type: application/json" -u admin1:admin1 http://localhost:5000/data/<id> <br />
               ```

cURL tool is used for testing.

## Local running steps:

docker container  ls -a
source .venv/bin/activate

End points and Syntax to use it : 
```
curl -X POST -H "Content-Type: application/json" -u admin1:admin1 -d '{"name": "John Doe", "age": 30, "city": "New York"}' http://localhost:5000/data
curl -X POST -H "Content-Type: application/json" -u admin1:admin1 -d '{"name": "Alan Turing", "age": 30, "city": "Sangli"}' http://localhost:5000/data
curl -X POST -H "Content-Type: application/json" -u admin1:admin1 -d '{"name": "Dennis Ritchi", "age": 30, "city": "Kolhapur"}' http://localhost:5000/data
curl -X POST -H "Content-Type: application/json" -u admin1:admin1 -d '{"name": "Brian Karnighan", "age": 30, "city": "Atpadi"}' http://localhost:5000/data
curl -X GET -H "Content-Type: application/json" http://localhost:5000/data/<id>
curl -u admin1:admin1 http://localhost:5000/data/<id>
curl -X PUT -H "Content-Type: application/json" -u admin1:admin1 -d '{"city": "Solapur"}' http://localhost:5000/data/<id>
curl -X DELETE-H "Content-Type: application/json" -u admin1:admin1 http://localhost:5000/data/<id>
```


## Running the application as Dockerized:

cd myproj/Docker  #here resides dockerfile used for starting container
docker build -t myflaskapp .          # we are building container here
docker run -p 5000:5000  myflaskapp   # we are running container here
docker ps                             # To check if container is started.

Now once above container is started we can run above cURL commands to perform CRUD operations.


Operating System:

```
~/myproj $ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04 LTS
Release:        24.04
Codename:       noble
```
