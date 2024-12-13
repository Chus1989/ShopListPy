from abc import ABC,abstractmethod

class InterfaceProductDAO(ABC):

    @abstractmethod
    def create_product(self,prod):
        pass
    @abstractmethod
    def show_products(self):
        pass
    @abstractmethod
    def show_oneproduct(self,id):
        pass
    @abstractmethod
    def modify_product(id,parameter,newparameter):
        pass
    @abstractmethod
    def delete_product(self,id):
        pass