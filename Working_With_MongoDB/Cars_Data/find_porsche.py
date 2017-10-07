import pdb
import pymongo
import pprint

def porsche_query():
    query = {}
    return query

def get_db(db_name):
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    pdb.set_trace()
    return db

def find_porsche(db, query):
    # For local use
    return db.cars.find(query)


if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    for car in results:
        pprint.pprint(car)

