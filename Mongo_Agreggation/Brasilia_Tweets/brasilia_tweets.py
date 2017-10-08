import pdb

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ ]
    pipeline_match = {"$match": {"user.time_zone":{"$in": ['Brasilia']}, "user.statuses_count": {"$gt": 100}} }
    pipeline_project = {"$project": {"followers": "$user.followers_count"}}
    pipeline_sort = {"$sort": {"followers": -1}}
    pipeline_limit = {"$limit": 1}
    pipeline = [pipeline_match, pipeline_project, pipeline_sort, pipeline_limit]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    pdb.set_trace()
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    assert result[0]["followers"] == 17209

