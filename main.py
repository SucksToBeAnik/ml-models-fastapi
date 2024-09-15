from fastapi import FastAPI, Depends, status
from fastapi.exceptions import HTTPException
from typing import Annotated
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from utils.db import engine, get_db_connection
from models import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "Welcome to the api"


@app.post("/user/{name}")
async def create_new_user(name: str, db: Annotated[Session, Depends(get_db_connection)]):
    try:
        new_user = User(name=name)
        db.add(new_user)
        db.commit()
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong when creating the user",
        )
