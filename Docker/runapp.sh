#!/bin/bash

mkdir -p /data/db    
# Create a directory for MongoDB
mongod --fork --logpath /var/log/mongod.log --dbpath /data/db   
# Start MongoDB
flask --app app.py run --host=0.0.0.0