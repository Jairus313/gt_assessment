from typing import Union
from fastapi import FastAPI

from model import login_cred

app = FastAPI()

@app.post("/login")
def read_root(item:login_cred):
    print(item)
    return {"username": item.username, "password": item.password}