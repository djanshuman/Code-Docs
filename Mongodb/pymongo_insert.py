from pymongo import MongoClient
import pymongo
import sys

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.people


insert1={'Name':'Dibyajyoti','Company':'Infosys','Age':24}
insert2={'_id':1001,'Name':'Rohit','Company':'TCS','Age':26}
insert_many1=([insert2,insert1])

def print_col():

	for i in mycol.find():
		print(i)

try:
	#mycol.insert_one(insert1)
	#mycol.insert_one(insert2)
	mycol.insert_many(insert_many1,ordered=False)
except Exception as e:
	print('Exception occured',e)

print('before insert_many')
print_col()
#print(insert1)
#print(insert2)
print('After insert_many')

def print_people():
	for i in mycol.find():
		print(i)

print_people()
