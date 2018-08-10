import pymongo

client = pymongo.MongoClient('127.0.0.1',port=27017)

db = client.zhihu

collection = db.message

collection.insert({'name':'小明','age':18})

cursor = collection.find()

for x in cursor:
    print(x['age'])