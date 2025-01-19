from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configure the PostgreSQL connection URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresqluser1Localhost_1234567@34.27.54.145432mono2micro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define a model for the 'users' table
class User(db.Model)
    __tablename__ = 'users'  # Table name in the database
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self)
        return fUser {self.username}

# Create the tables in the database
@app.before_request
def create_tables()
    # Ensure that tables are created before handling any requests
    db.create_all()

# Route to insert a new user into the 'users' table
@app.route('add_user', methods=['POST'])
def add_user()
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # Create a new user object
    new_user = User(username=username, email=email)

    try
        # Add the new user to the database and commit the transaction
        db.session.add(new_user)
        db.session.commit()
        return jsonify({message User added successfully!}), 201
    except Exception as e
        db.session.rollback()
        return jsonify({message Error occurred while adding user, error str(e)}), 500

# Route to fetch all users from the 'users' table
@app.route('get_users', methods=['GET'])
def get_users()
    users = User.query.all()
    users_list = [{id user.id, username user.username, email user.email} for user in users]
    return jsonify(users_list)

# Run the Flask application
if __name__ == '__main__'
    app.run(debug=True, host='0.0.0.0', port=5000)