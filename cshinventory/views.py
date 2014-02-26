from pyramid.view import view_config
from pyramid.response import Response
from models import DBSession, Owners, Item, Location, Barrowed
from CSHLDAP import CSHLDAP as ldap

#####
##### Pages
#####
@view_config(route_name='home', renderer='index.mak')
def home(request):
    
    user = getUser(request)
    return {'project': 'CSHInventory', 'username':user.username, 'page':"home" }

@view_config(route_name='addItem', renderer='index.mak')
def addItem(request):
    
    user = getUser(request)
    return {'project': 'CSHInventory', 'username':user.username, 'page':"item" }
 
@view_config(route_name='addLocation', renderer='index.mak')
def addLocation(request):
    
    user = getUser(request)
    return {'project': 'CSHInventory', 'username':user.username, 'page':"location" }

#####
##### AJAX Request Locations
#####
@view_config(route_name='createLocation', renderer='json')
def createLocation(request):
    print "Create Location!"

    user = getUser(request)
     
    req = request.POST
    name = req['name']
    roomNumber = req['roomNumber']
    owner = user
    
    loc =  addLocationDB(name, roomNumber, owner)

    print "Location:", loc
    return {}

#####
##### Helper Functions
#####
def getUser(request):
    
    username = request.headers["X-Webauth-User"]
    #now get the uuid
    uuid = ""
    print "UserName:", username
    print "UUID:", uuid

    if uuid == "":
        user = DBSession.query(Owners).filter_by(username = username).all()
    else:
        user = DBSession.query(Owners).filter_by(uuid = uuid).all()

    if len(user) == 0:
        cur = Owners(username, uuid)
        DBSession.add(cur)
        DBSession.commit()
        user = DBSession.query(Owners).filter_by(username = username).all()
        
        print "Made"

    if len(user) == 1:
        print "Found"
        cur = user[0]

    # if user == "zemon1":
    #     user = "admin"
   
    return cur

def addLocationDB(locName, roomNum, locOwner):
   
    exists = DBSession.query(Location).filter_by(owner = locOwner.id,
                                                 name = locName, 
                                                 roomNumber = roomNum).all()
    if len(exists) == 0:
        tempLoc = Location(owner.id, name, roomNum)
        DBSession.add(cur)
        DBSession.commit()
        loc = DBSession.query(Location).filter_by(id = tempLoc.id).all()
        print "Made Loc"
    if len(exists) == 1:
        print "Found Loc"
        loc = exists[0]

    return loc



