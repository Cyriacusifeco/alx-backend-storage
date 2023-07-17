#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs

    log_counts = db.nginx.count_documents({})
    get = db.nginx.count_documents({"method": "GET"})
    post = db.nginx.count_documents({"method": "POST"})
    put = db.nginx.count_documents({"method": "PUT"})
    patch = db.nginx.count_documents({"method": "PATCH"})
    delete = db.nginx.count_documents({"method": "DELETE"})
    status = db.nginx.count_documents({"path": "/status", "method": "GET"})

    print(f"{log_counts} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}\n\tmethod POST: {post}\n\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}\n\tmethod DELETE: {delete}")
    print(f"{status} status check")
