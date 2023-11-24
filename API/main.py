import sqlite3
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException 
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


# Pydantic Base Models:
class Message(BaseModel):
    message:str

class Client(BaseModel):
    id_client: int
    client_name: str
    client_lastname: str
    client_email: EmailStr
    client_password: str

class ClientSinID(BaseModel):
    client_name: str
    client_lastname: str
    client_email: EmailStr
    client_password: str


description = """
# FastAPI CRUD Template
CRUD Template with FastAPI and SQLite3
"""
# Create the FastAPI instance
app = FastAPI(
    title = "API REST Template", 
    description = description,
    version = "0.0",
    terms_of_service = "http://example.com/terms/",
    contact = {
        "name": "iAntonAMC",
        "url":"http://github.com/iAntonAMC",
        "email":"1721110125@utectulancingo.edu.mx",
    },
    license_info = {
        "name":"",
        "url":"",
    })

