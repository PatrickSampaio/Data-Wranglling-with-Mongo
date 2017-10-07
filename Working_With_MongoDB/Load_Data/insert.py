#!/usr/bin/env pytho

from autos import process_file
from pymongo import MongoClient
import pdb

def insert_autos(infile, db):
    data = process_file(infile)
    pdb.set_trace()
    for mongo_row in data:
       db.autos.save(mongo_row)
    
  
if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('../../fixtures/autos-small.csv', db)
    print(db.autos.find_one())
