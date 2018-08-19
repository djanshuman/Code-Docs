from pymongo import MongoClient
import sys
import datetime

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.scores

#update single record

def update_one(student_id):

	#fetch the document from db using student_id parameter
	
	pre_record=mycol.find_one({'student_id':student_id,'type':'homework'})
	print('Before update: ',pre_record)

	#fetch the unique _id for the document from the fetched document which is dictionary by passing _id as key to it for getting value mapped to it

	id_val=pre_record['_id']

	# update the db for the _id as adding one more entry review_date to the document

	matched=mycol.update_one({'_id':id_val},{'$set':{'review_date':datetime.datetime.utcnow()}})
	print('matched records count: ',matched.matched_count)

	record_updated=mycol.find_one({'student_id':student_id,'type':'homework'})
	print('updated record: ' , record_updated)

#update multiple record
def update_many_records():


        matched=mycol.update_many({},{'$set':{'review_date':datetime.datetime.utcnow()}})
        print('matched records count: ',matched.matched_count)

#removing the updated attribute from the document using $unset
def remove_entry():

	matched=mycol.update_many({'review_date':{'$exists':True}},{'$unset':{'review_date':1}})
	print('matched records with review_date',matched.matched_count)


#using replace_one function

def replace_one_method(student_id):
	
	record=mycol.find_one({'student_id':student_id,"type" : "homework"})
	print('before update in replace_one :',record)
	
	id_val=record['_id']
	
	record['review_date']=datetime.datetime.utcnow()
	
	mycol.replace_one({'_id':id_val},record)
	updated_value=mycol.find_one({'_id':id_val})
	print('updated value post replace_one :', updated_value)

#update_one(10)
#update_many_records()
#remove_entry()
replace_one_method(20)
