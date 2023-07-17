#!/usr/bin/env python3
"""Function list_all"""


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    if mongo_collection.count_documents({}) == 0:
        return []
    else:
        return mongo_collection.find()
