from typing import Union

from fastapi import FastAPI, Path, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/test")
async def update_item():
    print('success_test_api')
    return {"api": "woOOOork"}
