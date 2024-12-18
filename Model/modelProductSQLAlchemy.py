from sqlalchemy import Column,Integer, Boolean,String
from DB.connectionSQL import Base



class ModelProductSQLAlchemy(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String,nullable = False)
    purchased = Column(Boolean, nullable = False)
    number = Column(Integer, nullable = False)

