app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configure the PostgreSQL connection URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:Localhost_1234567@34.27.54.14:5432/mono2micro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define a model for the 'users' table
class User(db.Model):
    __tablename__ = 'users'  # Table name in the database
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.username}>"

# Create the tables in the database
@app.before_request
def create_tables():
    # Ensure that tables are created before handling any requests
    db.create_all()

# Route to insert a new user into the 'users' table
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # Create a new user object
    new_user = User(username=username, email=email)

    try:
        # Add the new user to the database and commit the transaction
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error occurred while adding user", "error": str(e)}), 500

# Route to fetch all users from the 'users' table
@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(users_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

jsbhullar2510@ajay-instance:/home/mauryaajay9594$ ^C
jsbhullar2510@ajay-instance:/home/mauryaajay9594$ ls
Dockerfile  Mono2Micro  __pycache__  app.py  commands.tct  df1  myenv  oldapp.py  requirements.txt
jsbhullar2510@ajay-instance:/home/mauryaajay9594$ cat Dockerfile 
# Step 1: Use the official Python image as the base image
FROM python:3.11-slim

# Step 2: Set environment variables to ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Set the working directory inside the container
WORKDIR /app

# Step 5: Copy the application code and requirements.txt into the container
COPY . /app

# Step 6: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Expose the port the Flask app will run on
EXPOSE 5000

# Step 8: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 9: Start the Flask app
CMD ["flask", "run"]

Dockerfile

# Step 1: Use the official Python image as the base image
FROM python:3.11-slim

# Step 2: Set environment variables to ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Set the working directory inside the container
WORKDIR /app

# Step 5: Copy the application code and requirements.txt into the container
COPY . /app

# Step 6: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Expose the port the Flask app will run on
EXPOSE 5000

# Step 8: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 9: Start the Flask app
CMD ["flask", "run"]

