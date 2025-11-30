#!/usr/bin/env python3
"""
Function to insert a new document into a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the collection
    Returns the id of the new document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
