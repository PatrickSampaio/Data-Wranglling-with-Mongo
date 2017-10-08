import pdb

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ ]
    pipeline_unwind = {"$unwind": "$entities.user_mentions"}
    pipeline_group = {"$group": {"_id": "$user.screen_name", "count" : { "$sum" : 1 } } }
    pipeline_sort = {"$sort": { "count" : -1 } }
    pipeline_limit = {"$limit": 1}
""" 
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""}
    pipeline = [pipeline_match, pipeline_project, pipeline_sort, pipeline_limit]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    pdb.set_trace()
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)

