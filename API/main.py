import sqlite3
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException 
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import API.models.clients as clients


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
        "name":"Apache 2.0",
        "url":"https://www.apache.org/licenses/LICENSE-2.0.html",
    })


# CORS
origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


# ROOT
@app.get(
    "/",
    response_model = Message,
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Confirm Connection",
    description = """
    Returns a JSON message to confirm the connection to the API
    parameters: None
    response: JSON message
    errors: 404 - Not Found
    """,
)
async def root():
    response = {"message":"API's connection confirmed"}
    return response

# GET ALL CLIENTS
@app.get(
    "/clients/all",
    response_model = List[Client],
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Get a list of clients",
    description = """
    Returns a JSON list with all the clients in the database\n
    errors:
        400 - Bad Request
        404 - Not Found
    """,
)
async def getAllClients():
    try:
        response = clients.all()
        return response
    except Exception as error:
        print(f"ERROR en getAllClients{error.args}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"message":f"Error: {error}"}
        )

# GET ONE CLIENT
@app.get(
    "/clients/{id_client}",
    response_model = Client,
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Get a client by ID",
    description = """
    Returns a JSON with the client's information\n
    errors:
        400 - Bad Request
        404 - Not Found
    """,
)
async def getClientByID(id_client: int):
    try:
        response = clients.clientByID(id_client)
        return response
    except Exception as error:
        print(f"ERROR en getClientByID{error.args}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"message":f"Error: {error}"}
        )

# CREATE ONE CLIENT
@app.post(
    "/clients/create",
    response_model = Message,
    status_code = status.HTTP_201_CREATED,
    summary = "Create a client",
    description = """
    Returns a JSON message that confirms the creation\n
    errors:
        400 - Bad Request
        404 - Not Found
    """,
)
async def createClient(client: ClientSinID):
    try:
        response = clients.create(client)
        return response
    except Exception as error:
        print(f"ERROR en createClient{error.args}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"message":f"Error: {error}"}
        )

# UPDATE ONE CLIENT
@app.put(
    "/clients/update/{id_client}",
    response_model = Message,
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Update a client",
    description = """
    Returns a JSON message that confirms the update\n
    errors:
        400 - Bad Request
        404 - Not Found
    """,
)
async def updateClient(id_client: int, client: ClientSinID):
    try:
        response = clients.update(id_client, client)
        return response
    except Exception as error:
        print(f"ERROR en updateClient{error.args}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"message":f"Error: {error}"}
        )

# DELETE ONE CLIENT
@app.delete(
    "/clients/delete/{id_client}",
    response_model = Message,
    status_code = status.HTTP_202_ACCEPTED,
    summary = "Delete a client",
    description = """
    Returns a JSON message that confirms the deletion\n
    errors:
        400 - Bad Request
        404 - Not Found
    """,
)
async def deleteClient(id_client: int):
    try:
        response = clients.delete(id_client)
        return response
    except Exception as error:
        print(f"ERROR en deleteClient{error.args}")
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"message":f"Error: {error}"}
        )
