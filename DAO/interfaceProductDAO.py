from abc import ABC,abstractmethod
from Singleton.SingletonMeta import singletonMeta
'''
JESUS JOYAS 2024 Shopping List test
This class is an abstract(ABC) interface for the dao implementation in json and slqalchemy
No instantiate this class
No return
no args
'''
#I use the singleton to instantiate one with the call(abc meta for the subclass)
class InterfaceProductDAO(ABC,metaclass = singletonMeta):

    @abstractmethod
    def create_product(self,id, name, purchased, number):
        pass
    @abstractmethod
    def show_products(self):
        pass
    @abstractmethod
    def show_oneproduct(self,id):
        pass
    @abstractmethod
    def modify_product(self,id,parameter,newparameter):
        pass
    @abstractmethod
    def delete_product(self,id):
        pass