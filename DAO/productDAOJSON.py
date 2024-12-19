
import json
import os
from .interfaceProductDAO import InterfaceProductDAO
from Model.modelProduct import ModelProduct

'''
JESUS JOYAS 2024 Shopping List test
This class is an implementation for json DAO methods of the product interface DAO
This add the CRUD methods for the json implementation in the controller logic
No return
no args
'''

class ProductDAOJSON(InterfaceProductDAO ):
    
    JSON = os.path.join(os.getcwd(),"DB","products.json")

    #The init method build in memory the data of the json    
    def __init__(self):
        self.dao_type = 'jsonDAO'
        
        self.data = self._loadJSON()
        
    '''
    This method load in memory the json file to operate with it
    Return : Json dictionary
    '''
    def _loadJSON(self):
        try:
            with open(self.JSON,"r") as file:
                
                return json.load(file)
            
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Founded an error {e}")

    '''
    This method create an instance of product and add the info to the json file
    This mehod add the new product to the loaded cache
    args:
        id:Int: The identifier of the product
        name: String: The name of the product
        Purchased: Bool: If it's purchased or not
        number: Int: The quantity to purchase
    Return: 0
    '''
    def create_product(self,id, name, purchased, number):
        
        prod = ModelProduct(id,name,purchased,number)
        newProduct = [{"id":prod.id},
                      {"name":prod.name},
                        {"purchased":prod.purchased},
                        {"number":prod.number}]
        self.data["items"].append(newProduct)

        try:
            with open(self.JSON, 'w') as file:
                json.dump(self.data,file,indent = 4)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Ha habido un error en el decode::{e}")
                 
    '''
    This method return a list of all the actual products in the data to operate
    with it
    args: 0
    return: Array of products
    '''
    def show_products(self):
        lstaProds = []
        for each in self.data["items"]:
            
            lstaProds.append(ModelProduct(each[0]["id"],each[1]["name"],each[2]["purchased"],each[3]["number"]))
        
        return lstaProds


    '''
    This method return the prodct with the argument id
    Args: Int: the id of the product to return
    Return: Class instance: The product with the id
    '''
    def show_oneproduct(self,id):
        prd = None
        for each in self.data["items"]:
            if each[0]["id"] == id:
                prd = ModelProduct(each[0]["id"],each[1]["name"],each[2]["purchased"],each[3]["number"])
        
        return prd
    
    '''
    This method modify one parameter of the product with the id passed as parameter
    args:
        Id:Int: The idof the producto to modify
        parameter:String: This is the parameter to modify
        newparameter: String: The new value of the parameter
    Return 0
    '''
    def modify_product(self,id,parameter=None,newparameter=None):
        for each in self.data["items"]:
            if each[0]["id"] == id:
                for i in range(1,4):
                    if parameter in each[i]:
                        each[i][parameter] = newparameter

        try:
            with open(self.JSON,"w") as file:
                json.dump(self.data,file,indent=4)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Error al modificar :: {e}")    
    
    '''
    This method delete a product of the data list and json with the id passed as 
    parameter
    args:
        Id:Int: The id of the product to eliminate
    return: 0
    '''
    def delete_product(self, id):
    
        self.data["items"] = [
            sublista for sublista in self.data["items"]
            if not any(diccionario.get("id") == id for diccionario in sublista)
        ]


        try:
            with open(self.JSON, "w") as file:
                json.dump(self.data, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Se ha encontrado un error: {e}")
