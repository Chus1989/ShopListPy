from .interfaceProductDAO import InterfaceProductDAO
from DB.connectionSQL import DatabaseConnection
from Model.modelProductSQLAlchemy import ModelProductSQLAlchemy
from Model.modelProduct import ModelProduct

'''
JESUS JOYAS 2024 Shopping List test
This class is an implementation of the abstract class InterfaceProductDAO
This implement the CRUD methods for sqllite using the ORM sql alchemy to make easy
this implementation
No return
no args
'''
class ProdutDAOSQLalchemy(InterfaceProductDAO):

    '''
    This init method create a session of the database and get the session to operate
    This have a argument named dao type to especify the type of DAO
    '''
    def __init__(self):
        self.dao_type = "sqlalchemy"
        db = DatabaseConnection()
        self.session = db.get_session()
    '''
    This method create a pduct and save it in the SQL database using SQL alchemy 
    Args:
        id: Int : the id of the product
        name:String : The name of the product
        purchased : Bool: If the product is purchased
        number: Int: The quantity to purchase of this product
    Return: 0
    '''
    def create_product(self,id = None, name = '', purchased = True, number = 0):
        newProduct = ModelProductSQLAlchemy(name = name,purchased = purchased,number = number)
        self.session.add(newProduct)
        self.session.commit()
    '''
    This methid using sql alchemy get the list of the products and create a list 
    of the instances of each product in the database
    Return: List: A list of the products
    '''
    def show_products(self):
        listProducts = []
        listquery = self.session.query(ModelProductSQLAlchemy).all()
        for each in listquery:
            listProducts.append(ModelProduct(each.id,each.name,each.purchased,each.number))

        return listProducts     
    
    '''
    This methdo returns a instance of product with the passed id
    Args:
        id:Int: This is the ID of the product
    return:class product instance: The instance of the searched product
    '''
    
    def show_oneproduct(self,id):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        return ModelProduct(obj.id,obj.name,obj.purchased,obj.number)
    
    '''
    This method modify a parameter of the product with the passed id
    arg:
        id:Int: The id of the product
        parameter:String: The name of the parameter to modify
        newparameter:String: The new parameter
    Return 0
    '''
    def modify_product(self,id,parameter,newparameter):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        if parameter == 'name':
            obj.name = newparameter
        if parameter == 'purchased':
            obj.purchased = newparameter
        if parameter == 'number':
            obj.number = newparameter
        self.session.commit()

    '''
    This method delete a product eith the passed id
    args:
        id: Int: The id of the product to delete
    '''
    
    def delete_product(self,id):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        self.session.delete(obj)
        self.session.commit()