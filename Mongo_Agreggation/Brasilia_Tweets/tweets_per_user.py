import pdb

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline_group = {"$group":
                                {"_id": "$user.id", "count": {"$sum" : 1}
                                ,"twitter_texts": { "$addToSet": "$text" }}}
    pipeline_sort = {"$sort": {"count": -1}}
    pipeline_limit = {"$limit": 5}

    pipeline = [pipeline_group, pipeline_sort, pipeline_limit]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    pdb.set_trace()
    import pprint
    pprint.pprint(result)
    assert len(result) == 5
    assert result[0]["count"] > result[4]["count"]
    sample_tweet_text = u'Take my money! #liesguystell http://movie.sras2.ayorganes.com'
    assert result[4]["tweet_texts"][0] == sample_tweet_text
    
