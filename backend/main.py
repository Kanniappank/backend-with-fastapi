# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Candy(BaseModel):
    id:int
    size:int

class CandySet(BaseModel):
    id:int
    candies:List[Candy]

candy_sets_global={}


@app.get("/")
def hello_world():
    return {"message": "Hello World"}

# Get candies


@app.get("/candies/{candie_set_id}")
def getCandies(candie_set_id:int):
    candies = [Candy(id=i,size=random.randint(1,10)) for i in range(10)]
    candie_set=CandySet(id=candie_set_id,candies=candies)
    candy_sets_global[candie_set_id] = candie_set
    return {"candies": candie_set}


@app.get("/{name}")
def hello_world_name(name):
    return "Hello World "+name




# Lick candies

@app.post("/lick/{candy_set_id}")
def lick_candies(candy_set_id):
    if candy_set_id not in candy_sets_global:
        raise HTTPException(status_code=404, detail="Candy set not found")
    candy_set = candy_sets_global[candy_set_id]
    return "Hello World "+name




# Bite Candies
