from fastapi import FastAPI
from json_db import JsonDB
from product import Product
import indb


app = FastAPI()

productDB = JsonDB(path="data/products.json")

@app.get("/products")
def get_products():
    products = productDB.read()
    return { "products" : products }

@app.post("/products")
def create_product(product: Product):

    productDB.insert(product)

    return {"status": "produto adicioado com sucesso!"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    data = productDB.read()

    for product in data["products"]:
        if product["id"] == product_id:
            return product
        
        return {"status": "produto não encontrado!"}
    
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    data = productDB.read()

    data["products"] = [
        p for p in data["products"] if p["id"] != product_id
    ]
    
    productDB.insert(data)

    return {"status": "produto deletado com sucesso!"}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    data = productDB.read()

    for p in data["products"]:
        if p["id"] == product_id:
            p["name"] = product.name
            p["price"] = product.price

    productDB.write(data)

    return {"status": "produto atualizado com sucesso!"}

