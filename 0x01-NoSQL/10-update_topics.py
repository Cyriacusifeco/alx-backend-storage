#!/usr/bin/env python3
"""Function update_topics """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a doc based on name """
    mongo_collection.update_many({"name": name},
                                 {'$set': {"topics": topics}})
