# Python Code to fetch JSON format data through API call and inserting to MongoDB database ***
# We have created database= mydatabase and collections=Customers ***


import requests
from pprint import pprint
response = requests.get("https://api.data.gov.in/resource/31f36e27-498d-4dd6-ae83-37bb1f8f5383?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=50")
import json
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.mydatabase
mycol=db.Customers
x=response.content

#Convert received string to JSON object of dict type
import json
json_string=x
obj=json.loads(json_string)
x=mycol.insert_one(obj)
for i in mycol.find():
	pprint(i)
print("\n")
print("Number of documents in collection",mycol.find().count())
print("No of insertion and updation object id",x)
print("Specific ID",x.inserted_id)
