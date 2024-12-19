from sqlalchemy import Column,Integer, Boolean,String
from DB.connectionSQL import Base


'''
This is a sql alchemy model to create a table in the database
this class heredates of the declarative base of the connection class
the tablename is products and each of the columns recives the args of each column
'''
class ModelProductSQLAlchemy(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String,nullable = False)
    purchased = Column(Boolean, nullable = False)
    number = Column(Integer, nullable = False)

