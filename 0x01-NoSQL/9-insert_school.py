#!/usr/bin/env python3
""" function insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in collection based on kwargs """
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id
