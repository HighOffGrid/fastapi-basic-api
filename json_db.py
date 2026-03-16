from pydantic import BaseModel
import json

from product import Product

class JsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path)   
        data = json.loads(f.read())
        f.close() 
        return data
    
 
    def insert(self, product: Product):
        data = self.read()

        data["products"].append(product.model_dump())


        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
  
       
  