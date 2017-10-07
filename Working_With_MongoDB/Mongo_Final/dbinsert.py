#"""
#Complete the insert_data function to insert the data into MongoDB.
#"""

import json

def insert_data(data, db):
    current_collection = db.get_collection("arachnid")
    current_collection.insert(data)


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples
    db.create_collection("arachnid")

    with open('../../fixtures/arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()
