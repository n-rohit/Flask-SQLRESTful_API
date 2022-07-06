import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # We use the brackets here to inform Python that the brackets represent a Tuple; and that they are not just a useless pair of brackets
        row = result.fetchone() # Retrieving the first row from the Result set
        if row:
            user = cls(*row) #* Same as cls(row[0], row[1], row[2])
        else:
            user = None 
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)) # We use the brackets here to inform Python that the brackets represent a Tuple; and that they are not just a useless pair of brackets
        row = result.fetchone() # Retrieving the first row from the Result set
        if row:
            user = cls(*row) #* Same as cls(row[0], row[1], row[2])
        else:
            user = None 
        
        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This Field cannot be left Blank!"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This Field cannot be left Blank!"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data["username"]): # If this value is not None
            return {"message": "A User with that Username already exists"}, 400 
        # By putting this if condition here, we are not running any connection or cursor code if there is new user being created with an existing username

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" # SInce the ID value is Auto Incrementing, we should put id value as NULL here
        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()
        return {"message": "User Created Successfully."}, 201