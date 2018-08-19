from pymongo import MongoClient
import sys

# establish a connection to database

connection=MongoClient('localhost',27017)

# Get a handle to school database

db=connection.school
mycol=db.scores

query1={'student_id':10}
query2={'type':'exam','score':{'$gt':60,'$lt':90}}

#projection

projection={'student_id':1,'score':1,'_id':0}

def find_one():
        try:
            x=mycol.find_one(query1)
            print(i)
        except Exception as e:
            print('exception occured',type(e),e)

def find():
        try:
                x=mycol.find(query2,projection)
                counter=0
                for i in x:
                        counter+=1
                        if (counter<=10):
                                print(i)

        except Exception as e:
            print('exception occured',type(e),e)

print(mycol.count())
find()
