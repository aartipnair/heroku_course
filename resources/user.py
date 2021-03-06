import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be empty."
      
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be empty."
      
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"User already exists"},400

        user=UserModel(**data)
        user.save_to_db()


        '''connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"

        cursor.execute(query,(data['username'],data['password']))
        

        connection.commit()
        connection.close()'''

        return {"message":"User created successfully."},201


class User(Resource):

    @classmethod
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not found!'},404
        return user.json()
    

    @classmethod
    def delete(self,user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not found!'},404

        user.delete_from_db()
        return {'message':'User deleted.'},200






