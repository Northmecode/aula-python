from pymongo import MongoClient, collection
from pandas import DataFrame

# Connection string from MongoDB - Google Cloud - from pymongo
CONNECTION_STRING = 'mongodb+srv://estudo-i-user:Griclocalnt01@cluster0.nhrrm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# Connection function MongoDB
client = MongoClient(CONNECTION_STRING)

db = client.Produtos
collection_name = db.customers
item_details = collection_name.find()

for item in item_details:
    #Print each document
    print(item['name'],item['email'])
