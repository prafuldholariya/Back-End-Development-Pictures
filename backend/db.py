import pymongo
from flask import jsonify
from bson import json_util
# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
userdatabse = client["userdata"]
collection_personalinfo = userdatabse["personal_info"]

class dataBase:

    def __init__(self):
        if collection_personalinfo.find().limit(1):
            d = collection_personalinfo.delete_many({})
            print("Clean Database Total Record",d.deleted_count)

        mylist = [
            { "id" : 1, "name": "Kesav", "address": "Madhura st 652", "age" : 26},
            { "id" : 2, "name": "Madhav", "address": "Mountain 21", "age" : 26},
            { "id" : 3, "name": "IShvar", "address": "Sky uppon 345", "age" : 26},
            { "id" : 4, "name": "Vijay", "address": "Valley 345", "age" : 26},
            { "id" : 5, "name": "Ram", "address": "Ayodhya Ultimate", "age" : 26}
        ]
        resultinsert = collection_personalinfo.insert_many(mylist)
        if resultinsert.inserted_ids.count :
            print("Inserted Data Successfully")
    
    def inserOneData(self,id):
        check_data = collection_personalinfo.find_one({'id':id})
        if check_data :
            print("Data already exist")
            return False
        add = { "id" : id, "name": "Shankar", "address": "Kedarnath st 652", "age" : 126}
        result_add = collection_personalinfo.insert_one(add)
        print("insert", result_add)
        return True
    
    def findData(self):
        find_result = collection_personalinfo.find()
        return find_result
    
    def findOneData(self,id):
        find_result = collection_personalinfo.find_one({'id':id})
        if not find_result:
            return {"message": f"data with id {id} not found"}, 404
        return parse_json(find_result)
    
    def deleteOneData(self, id):
        find_result = collection_personalinfo.delete_one({'id':id})
        return find_result
    
    def updateOneData(self, id):
        # Update a document
        update_query = {"id": id}
        new_values = {"$set": {"age": 35}}
        update_result = collection_personalinfo.update_one(update_query, new_values)
        return update_result

def parse_json(result):
    result = json_util.dumps(result)
    return jsonify(result), 200
