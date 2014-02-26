from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Unicode, String, ForeignKey, Column, LargeBinary, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
import datetime

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class Owners(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    username = Column(String(128))
    uuid = Column(String(128))

    item = relationship("Item")
    barrow = relationship("Barrowed")

    def __init__(self, name, uuid=""):
        self.username = name
        self.uuid = uuid

    def __str__(self):
        string = "Owners: {" + str(self.id) + ": " + str(self.name) + "}"
        return string

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, ForeignKey('owners.id'))
    name = Column(String(128))
    roomNumber = Column(String(128))

    def __init__(self, ownerId, name, roomNumber):
        self.ownerId = ownerId
        self.name = name
        self.roomNumber = roomNumber

    def __str__(self):
        string = "Location: {" + str(self.id)
        string += "\nOwnerId: " + str(self.ownerId) 
        string += "\nName: " + str(self.name) 
        string += "\nRoomNumber: " + str(self.roomNumber) 
        string += "}"
        return string

class Barrowed(Base):
    __tablename__ = 'barrowed'
    id = Column(Integer, primary_key=True)
    itemId = Column(Integer, ForeignKey('item.id'))
    barrowerId = Column(Integer, ForeignKey('owners.id'))
    start = Column(DateTime, default=datetime.datetime.utcnow)
    end = Column(DateTime, nullable=True)

    def __init__(self, itemId, barrowerId):
        self.itemId = itemId
        self.barrowerId = barrowerId

    def __str__(self):
        string = "Barrowed: {" + str(self.id) + ": " + str(self.itemId) + "}"
        string += "\nBarrowerId: " + str(self.barrowerId) 
        string += "\nStart: " + str(self.start) 
        string += "\nEnd: " + str(self.end) 
        return string

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, ForeignKey('owners.id'))
    locId = Column(Integer, ForeignKey('location.id'))
    barcode = Column(String(128))
    cost = Column(Integer)
    desc = Column(String(128))

    def __init__(self, ownerId, locId, barcode, desc, cost=-1):
        self.ownerId = ownerId
        self.locId = locId
        self.barcode = barcode
        self.desc = desc
        self.cost = cost


    def __str__(self):
        string = "Item: {" + str(self.id) + ": " 
        string += "\nOwnerId: " + str(self.ownerId) 
        string += "\nLocId: " + str(self.locId) 
        string += "\nBarcode: " + str(self.barcode) 
        string += "\nDesc: " + str(self.desc) 
        string += "\nCost: " + str(self.cost) 
        return string


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all(engine, checkfirst=False)
    DBSession.commit()
