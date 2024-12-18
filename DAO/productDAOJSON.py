
import json
import os
from .interfaceProductDAO import InterfaceProductDAO
from Model.modelProduct import ModelProduct
from Singleton.SingletonMeta import singletonMeta
from abc import ABCMeta,ABC



class ProductDAOJSON(InterfaceProductDAO ):
    
    JSON = os.path.join(os.getcwd(),"DB","products.json")

    def __init__(self):
        self.dao_type = 'jsonDAO'
        
        self.data = self._loadJSON()
        

    def _loadJSON(self):
        try:
            with open(self.JSON,"r") as file:
                
                return json.load(file)
            
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Founded an error {e}")


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
                 
    
    def show_products(self):
        lstaProds = []
        for each in self.data["items"]:
            
            lstaProds.append(ModelProduct(each[0]["id"],each[1]["name"],each[2]["purchased"],each[3]["number"]))
        
        return lstaProds


    
    def show_oneproduct(self,id):
        prd = None
        for each in self.data["items"]:
            if each[0]["id"] == id:
                prd = ModelProduct(each[0]["id"],each[1]["name"],each[2]["purchased"],each[3]["number"])
        
        return prd
    
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


    def delete_product(self, id):
        self.data["items"] = [sublista for sublista in self.data["items"] if not any(diccionario.get("id") == id for diccionario in sublista)]

        try:
            
            with open(self.JSON, "w") as file:
                json.dump(self.data, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Se ha encontrado un error: {e}")

