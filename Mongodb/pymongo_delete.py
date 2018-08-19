from pymongo import MongoClient
import sys

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.scores

def delete_one_method(student_id):

	record=mycol.delete_one({'student_id':student_id})
	print(record.deleted_count)


	record_display=mycol.find({'student_id':student_id})
	print(record_display)



def delete_many(student_id):
       record=mycol.delete_many({'student_id':student_id})
       print(record.deleted_count)
       record_display=mycol.find({'student_id':student_id})
       print('fetched result: ',record_display)


#delete_one_method(20)
delete_many(20)
