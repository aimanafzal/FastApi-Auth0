# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

from unittest import result
from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer

from utils import VerifyToken
token_auth_scheme = HTTPBearer()

app = FastAPI()



@app.get("/api/public")
def public():
    result = {
        "status": "success",
        "msg"   : ("Hello from a public endpoint! You don't need to be authenticated to access this.")
    }
    return result

@app.get("/api/private")
def private (response: Response, token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    
    return result