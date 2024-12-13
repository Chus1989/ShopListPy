from interfaceProductDAO import InterfaceProductDAO
import os
import json

class Prod:
    def __init__(self):
        self.name = "ajo"
        self.purchased = False
        self.num = 10

class ProductDAOJSON(InterfaceProductDAO):

    JSON = os.path.join(os.getcwd(),"DB","products.json")

    def __init__(self):
        prod = Prod()
        self.data = self._loadJSON()
        self.modify_product(1,"name","pamon")
        

    def _loadJSON(self):
        try:
            with open(self.JSON,"r") as file:
                
                return json.load(file)
            
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Founded an error {e}")


    def create_product(self,prod):

        newID = len(self.data.keys())+1
        
        self.data[newID] = [{"name":prod.name},
                            {"purchased":prod.purchased},
                            {"number":prod.num}]

        try:
            with open(self.JSON, 'w') as file:
                json.dump(self.data,file,indent = 4)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Ha habido un error en el decode::{e}")
                 
    
    def show_products(self):
        for i,j in self.data.items():
            for each in i:
                print(self.data[each])


    
    def show_oneproduct(self,id):
        for each in self.data.keys():
            if str(id) == each:
                print(self.data[each])
    
    def modify_product(self,id,parameter=None,newparameter=None):
        if self.data[str(id)]:
            for i in self.data[str(id)]:
                
                if (parameter and newparameter):
                    try:
                        if i[parameter]:
                    
                            i[parameter] = newparameter
                    except:
                        print("no existe el valor")
                else:
                    raise ValueError

        try:
            with open(self.JSON,"w") as file:
                json.dump(self.data,file,indent=4)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"Error al modificar :: {e}")    


    def delete_product(self,id):
        
        if self.data[str(id)]:
            del self.data[str(id)]
        
        try:
            with open(self.JSON,"w") as file:
                json.dump(self.data, file, indent = 4)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            print(f"se ha encontrado un error : {e}")


ProductDAOJSON()