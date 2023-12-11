from typing import Union
from fastapi import FastAPI

from model import login_cred
from db import SessionLocal, engine, Base




app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def read_root(item:login_cred):
    
    return {"username": item.username, "password": item.password}