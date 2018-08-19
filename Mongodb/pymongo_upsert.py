from pymongo import MongoClient
import sys

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.fruits



def upserts():
	mycol.drop()

	mycol.update_one({'thing':'apple'},{'$set':{'color':'red'}},upsert=True)
	mycol.update_many({'thing':'banana'},{'$set':{'color':'yellow'}},upsert=True)
	mycol.replace_one({'thing':'peach'},{'color':'green'},upsert=True)
	mycol.replace_one({'_id':1001},{'color':'blue'},upsert=True)
	apple=mycol.find_one({'thing':'apple'})
	print(apple)
	banana=mycol.find_one({'thing':'banana'})
	print(banana)
	peach=mycol.find_one({'thing':'peach'})
	idOne=mycol.find_one({'_id':1001})
	print(idOne)

	'''it will give None as result as 'thing:peach' is a selector in replace_one and color:green is the record to be inserted. If we query the collctn we can find 'color':'green'
	value in the col inserted in the run '''
	print(peach)


upserts()	
