#!/usr/bin/env python3
""" Function module """


def schools_by_topic(mongo_collection, topic):
    """ Returns list of school having a specific topic """
    return mongo_collection.find({"topics": topic})
