from pymongo import MongoClient


Client = MongoClient()
myclient = MongoClient('localhost', 27017)

my_database = myclient["GFG"]
my_collection = my_database["pymongo"]

# number of documents in the collection
mydoc = my_collection.find().count()
print("The number of documents in collection : ", mydoc)
