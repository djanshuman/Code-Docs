import pymongo
import sys

# establish a connection to database

connection=pymongo.MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.counters



def update_counter(name):
	counter=mycol.find_one_and_update(filter={'type':name},
					  update={'$inc':{'value':1}},
					  upsert=True,
					  return_document=pymongo.ReturnDocument.AFTER)
	print(counter['value'])
	


update_counter('uid')
update_counter('uid')
update_counter('uid')
	
	
