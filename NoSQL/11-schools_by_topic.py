#!/usr/bin/env python3
"""
Module to search MongoDB schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic (string): topic searched
    """
    return list(mongo_collection.find({ "topics": topic }))
