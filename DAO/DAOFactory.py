
from .productDAOJSON import ProductDAOJSON
from .productDAOSQLalchemy import ProdutDAOSQLalchemy

'''
JESUS JOYAS 2024 shopping list 
This clas
'''
class DAOfactory:

    def get_dao(self,dao_type):
        if dao_type == "json_dao":
            return ProductDAOJSON()
            
        if dao_type == "sqlalchemy_dao":
            return ProdutDAOSQLalchemy()
        
