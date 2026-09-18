from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource,reqparse,marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)   # creating a Flask application instance named app. This instance will be used to configure the application, define routes, and handle requests.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'   # configuring the Flask application to use a SQLite database named data.db.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # configuring the Flask application to disable SQLAlchemy's event system, which is not needed in this project and can save some overhead.
db=SQLAlchemy(app)   # creating a SQLAlchemy object named db, which will be used to interact with the database. It is initialized with the Flask application instance app.
api=Api(app)   

class UserModel(db.Model): #creating the UserModel class which inherits from db.Model, representing the users table in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self): #__repr__ is a special method used to define how an object is represented as a string. It is useful for debugging and logging purposes.
        return f"<User: {self.name}>,<User Email: {self.email}>" # f is used to format the string with the values of name and email
    
with app.app_context():  # app_context is used to ensure that the database operations are performed within the application context
    db.create_all()
    
# Request parser is used to parse and validate incoming request data
user_Arguments = reqparse.RequestParser()
user_Arguments.add_argument("name", type=str, help="Name of the user is required", required=True)
user_Arguments.add_argument("email", type=str, help="Email of the user is required", required=True)



@app.route('/')
def home():
    return ("<h1>Welcome to the API</h1>")


#_____CREATING A NEW USER

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get JSON data from the request body
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    new_user = UserModel(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name, "email": new_user.email}}), 201
 
 
#_______GET ALL USERS 
         
@app.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users]), 200


#_________GET USERS BY ID

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserModel.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
    
#___________GET USERS BY EMAIL

@app.route('/users/email/<string:email>', methods=['GET'])
def get_user_by_email(email):
    user = UserModel.query.filter_by(email=email).first()
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
#_____________ADD
   
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserModel.query.get(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.name = data.get('name', user.name) # y = (get x, if no x keep y)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "email": user.email}}), 200

#_________UPDATE 

@app.route('/users/<int:user_id>', methods=['PATCH'])
def edit_user(user_id):
    data = request.get_json()
    user = UserModel.query.get(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    return jsonify({"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "email": user.email}}), 200
 
#______________DELETE 
 
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True,port=8080)