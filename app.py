import os
from flask import Flask
from flask_restful import Api 
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister,User
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTION'] = True
app.secret_key='1996'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app,authenticate,identity) # /auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(User,'/user/<int:user_id>')

if __name__ == '__main__':
    
    db.init_app(app)
    app.run(port=5002,debug=True)



