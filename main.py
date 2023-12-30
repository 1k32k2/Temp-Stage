from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

user = os.environ['USER']
password = os.environ['PASSWORD']

uri = f"mongodb+srv://{user}:{password}@cluster0.h0wrxfe.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

mydb = client["stage"]
mycol = mydb["id"]

id = 1234

mydict = { "id": "1234"}

x = mycol.insert_one(mydict)