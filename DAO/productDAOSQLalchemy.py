from .interfaceProductDAO import InterfaceProductDAO
from DB.connectionSQL import DatabaseConnection
from Model.modelProductSQLAlchemy import ModelProductSQLAlchemy
from Model.modelProduct import ModelProduct


class ProdutDAOSQLalchemy(InterfaceProductDAO):

    def __init__(self):
        self.dao_type = "sqlalchemy"
        db = DatabaseConnection()
        self.session = db.get_session()
    
    def create_product(self,id = None, name = '', purchased = True, number = 0):
        newProduct = ModelProductSQLAlchemy(name = name,purchased = purchased,number = number)
        self.session.add(newProduct)
        self.session.commit()
    
    def show_products(self):
        listProducts = []
        listquery = self.session.query(ModelProductSQLAlchemy).all()
        for each in listquery:
            listProducts.append(ModelProduct(each.id,each.name,each.purchased,each.number))

        return listProducts     
    
    def show_oneproduct(self,id):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        return ModelProduct(obj.id,obj.name,obj.purchased,obj.number)
    
    def modify_product(self,id,parameter,newparameter):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        if parameter == 'name':
            obj.name = newparameter
        if parameter == 'purchased':
            obj.purchased = newparameter
        if parameter == 'number':
            obj.number = newparameter
        self.session.commit()
    
    def delete_product(self,id):
        obj = self.session.query(ModelProductSQLAlchemy).filter_by(id = id).first()
        self.session.delete(obj)
        self.session.commit()