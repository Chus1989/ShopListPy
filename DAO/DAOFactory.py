
from .productDAOJSON import ProductDAOJSON
from .productDAOSQLalchemy import ProdutDAOSQLalchemy

'''
JESUS JOYAS 2024 shopping list 
This class creates the necessary methods for the implementation of only one 
instance of the DAO type(sql, json)
Return 0
'''
class DAOfactory:

    '''
    This method return one instance of the DAO classes (sql, json)
    Arg: dao_type: String: The need of the instance to generate
    Return: class instance
    '''
    def get_dao(self,dao_type):
        if dao_type == "json_dao":
            return ProductDAOJSON()
            
        if dao_type == "sqlalchemy_dao":
            return ProdutDAOSQLalchemy()
        
