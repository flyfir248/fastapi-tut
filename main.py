from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None

inventory = {
    1: {
        "name": "milk",
        "price": 3.99,
        "brand": "premium"
    },
    2: {
        "name": "bread",
        "price": 2.49,
        "brand": "artisan"
    },
    3: {
        "name": "eggs",
        "price": 1.99,
        "brand": "organic"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item in inventory")):
    return inventory.get(item_id, {"Data": "Item not found"})

@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test : int):
    for item_id, item_info in inventory.items():
        if item_info["name"] == name:
            return item_info
    #return {"Data": "Item not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found.")


@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        # return {"Error":"Item ID already exists."}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID already exists.")

    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int, item:Item):
    if item_id not in inventory:
        # return {"Error":"Item ID does not exist."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found.")

    if item.name != None :
        inventory[item_id].name = item.name

    if item.price != None :
        inventory[item_id].price = item.price

    if item.brand != None :
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(...,description = "The ID of the")):
    if item_id not in inventory:
        # return {"Error" : "ID does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found.")

    del inventory[item_id]
    return  {"Success":"Item deleted"}
