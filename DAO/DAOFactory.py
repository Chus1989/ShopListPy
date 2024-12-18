
from .productDAOJSON import ProductDAOJSON

'''
JESUS JOYAS 2024 shopping list 
This clas
'''
class DAOfactory:

    def get_dao(self,dao_type):
        if dao_type == "json_dao":
            prod = ProductDAOJSON()
            return prod
        if dao_type == "sqlalchemy_dao":
            return None
        
