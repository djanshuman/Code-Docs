from pymongo import MongoClient
import pymongo
import sys

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.scores

'''mongodb follows a sequence of Sort -> Skip -> Limit rule for every iteration. It skips the element from top irrespective of asc or dsc and then
returns exact number of documents asked in limit function. for example after sort and skip if element left is 7 then it iterates and pull more 3 
records from documents to return exact 10'''

#Two ways to write code for sort,skip,limit. Below are examples to retrieve data based on single key and multiple keys

query={}
#x=mycol.find(query)
#x.limit(10)
#x.skip(3)
#x.sort('student_id',pymongo.DESCENDING)

#for i in x:
#	print(i)

x1=mycol.find(query).skip(3).limit(10)

#for multiple selection attribute we use multiple tuples in a list

x1.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

for i in x1:
	print(i)



