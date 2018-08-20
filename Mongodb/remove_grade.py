# Dataset :- 'grades.json' in -> ' Mongodb/Resources/grades.json ' path in github.
/* This question is part of M101P: MongoDB for Developers Course by MongoDB University. The requirement here is to:-
Remove the grade of type "homework" with the lowest score for each student from the dataset. 
Since each document is one grade, it should remove one document per student.
So it means from every student_id there exists 4 'type' out of which two 'type' are 'homework' . 
We have to remove the lowest score out of two 'type':'homework' document.

The up and running code in pymongo is below:- */

import pymongo
import sys

#establish a connection to database

connection=pymongo.MongoClient('localhost',27017)
#Get a handle to students database

db=connection.students
mycol=db.grades

def remove_documents():
        pipe=[
        {'$match':{'type':'homework'}},
        {'$group':{'_id':'$student_id','minscore':  {'$min':'$score'}}}
        ,{'$sort':{'_id':1}}
             ]
        result_cursor=mycol.aggregate(pipeline=pipe)
        counter=0

        for i in result_cursor:
            query={'student_id':i['_id'],'score':i['minscore']}
            del_record=mycol.delete_one(query)
            if (int(del_record.deleted_count) > 0):
                    counter+=1
            else:
                    continue
        print(counter)
remove_documents()

