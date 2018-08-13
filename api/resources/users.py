import json
from config.mongo import database
from marshmallow import fields, Schema
import falcon

class UsersResource(object):

    def on_get(self, req, resp):
        users = []
        for user in database.users.find():
            users.append({"id": str(user["_id"]), 'username': user["user_name"], 'name': user["name"], 'age': user["age"]})
        
        resp.body = json.dumps(users, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        user = json.loads(req.bounded_stream.read())
        database.users.save(user)
        resp.body = json.dumps({"message": "user created!"})
        resp.status = falcon.HTTP_201
