import bottle
from pymongo import MongoClient


@bottle.route('/')
def home_page():
    # Connecting to localhost and assigning its instance to client
    client = MongoClient('localhost', 27017)

    # Connecting to database video and storing instance to db
    db=client.video
    # Here we are storing the database.collections to a variable (Handler)  so that we can directly use mycol while operation
    mycol=db.movies	
    #mycol.insert_one({'_id':100,'Name':'Barfi','Rating':9.2})
    x=mycol.find()
    for i in x:
    	print(i)

    # Bottle framework Code to assign fruit list to template hello_world
    mythings = ['apple', 'orange', 'banana', 'peach']
    #return bottle.template('hello_world', username='Andrew', things=mythings)
    return bottle.template('hello_world', {'username':"Anshuman", 'things':mythings})


@bottle.post('/favourite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit_name")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"
    
    # Below code set cookie to value obtained from form passed by user
    bottle.response.set_cookie("fruit_name", fruit)

    '''After cookie value is set , it re-directs to /show_fruit page , here if user refresh the page then it reduces overhead and display stored cookie value '''
    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():

    # Fetch cookie value and display to user	
    fruit = bottle.request.get_cookie("fruit_name")
	
    # The fruit_template has html code to display value of fruit passed by user in hello_world template
    return bottle.template('fruit_template.tpl', {'fruit_name':fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8082)

