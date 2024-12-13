from sqlalchemy import Column,Integer, Boolean,String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class ModelProductSQLAlchemy(base):
    __tablename__ = "products"
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String,nullable = False)
    purchased = Column(Boolean, nullable = False)
    number = Column(Integer, nullable = False)

