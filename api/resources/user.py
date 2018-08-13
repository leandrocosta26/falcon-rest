import json
from config.logger import logger
from config.mongo import database
from bson.objectid import ObjectId
import falcon

class UserResource(object):
    def on_get(self, req, resp, _id):
        user = database.users.find_one({"_id": ObjectId(_id)})
        response = {
                "id": str(user["_id"]), 
                'username': user["user_name"], 
                'name': user["name"], 
                'age': user["age"]
        }
        resp.body = json.dumps(response, ensure_ascii=False)
        resp.status = falcon.HTTP_200
        

    def on_put(self, req, resp, _id):
        database.users.find_one_and_replace({"_id": ObjectId(_id)}, req.bounded_stream.read())
        resp.body = json.dumps({"message": "user update!"})
        resp.status = falcon.HTTP_202

    def on_delete(self, req, resp, _id):
        database.users.find_one_and_delete({"_id": ObjectId(_id)})
        resp.body = json.dumps({"message": "user removed!"})
        resp.status = falcon.HTTP_204
