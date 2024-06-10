# Use the official image as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# install libssl1.1	
RUN apt-get update && apt-get install -y gnupg wget && \
    wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
    dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb


# Install MongoDB and its prerequisites
RUN apt-get update && \
    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list && \
    apt-get update && apt-get install -y mongodb-org

# Starting MongoDB service
RUN mkdir -p /data/db    # Create a directory for MongoDB
#RUN mongod  --fork --bind_ip_all --logpath /var/log/mongod.log --dbpath /data/db   # Start MongoDB

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

RUN chmod +x runapp.sh

# Define environment variable
#ENV FLASK_APP app.py


# Run app.py when the container launches
CMD ["bash", "./runapp.sh"]
