import sys
import pymongo as pm

conn = pm.MongoClient("mongodb://localhost")

db = conn.test
users = db.users

doc = {"first_name": "Dong-Hoon", "last_name": "Lee"}
print(doc)
print("about to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("first insert failed: ", e)

print(doc)
print("insert again..")

try:
    users.insert_one(doc)
except Exception as e:
    print("second insert failed: ", e)
