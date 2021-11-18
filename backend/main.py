from sqlalchemy import create_engine, func, Integer, String, Column, DateTime, exists, desc, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import rank

#import flask
from flask import Flask
from flask_restful import Api, Resource

# TODO:
# - parse the node links
# - generate sql query
# - deynamically create classes based on the table names

base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
db = Session(engine)
base.metadata.create_all(engine)
conn = engine.connect()

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def post(self):
        print('post')
        return "hi"


api.add_resource(Main, '/')

app.run(debug=True)