import sqlite3
from fastapi.responses import JSONResponse


# GET ALL
def all():
    try:
        with sqlite3.connect("SQL/database.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT id_client, client_name, client_lastname, client_email, client_password FROM clients;")
            clients = cursor.fetchall()
            clients_list = []
        if clients == []:
            return JSONResponse(status_code = 404, content = {"message":"There are no clients in database"})
        else:
            for client in clients:
                clients_list.append({
                    "id_client":client[0],
                    "client_name":client[1],
                    "client_lastname":client[2],
                    "client_email":client[3],
                    "client_password":client[4],
                })
            return clients_list
    except Exception as error:
        print(f"Error in clients.all: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model method dropped an error: {error}"
        )

# GET ONE
def clientByID(id_client: int):
    try:
        with sqlite3.connect("SQL/database.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT id_client, client_name, client_lastname, client_email, client_password FROM clients WHERE id_client = ?;", (id_client,))
            client = cursor.fetchone()
        if client == None:
            return JSONResponse(status_code = 404, content = {"message":"Client not found"})
        else:
            client = {
                "id_client":client[0],
                "client_name":client[1],
                "client_lastname":client[2],
                "client_email":client[3],
                "client_password":client[4],
            }
            return client
    except Exception as error:
        print(f"Error in clients.clientByID: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.clientByID method dropped an error: {error}"
        )

# CREATE ONE
def create(client):
    try:
        with sqlite3.connect("SQL/database.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("INSERT INTO clients (client_name, client_lastname, client_email, client_password) VALUES (?,?,?,?);", (client.client_name, client.client_lastname, client.client_email, client.client_password))
            cnxn.commit()
            return JSONResponse(status_code = 201, content = {"message":"Client created successfully"})
    except Exception as error:
        print(f"Error in clients.create: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.create method dropped an error: {error}"
        )

# UPDATE ONE
def update(id_client: int, client):
    try:
        with sqlite3.connect("SQL/database.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM clients WHERE id_client = ?;", (id_client,))
            client = cursor.fetchone()
        if client == None:
            return JSONResponse(status_code = 404, content = {"message":"Client not found"})
        else:
            cursor.execute("UPDATE clients SET client_name = ?, client_lastname = ?, client_email = ?, client_password = ? WHERE id_client = ?;", (client.client_name, client.client_lastname, client.client_email, client.client_password, id_client))
            cnxn.commit()
            return JSONResponse(status_code = 202, content = {"message":"Client updated successfully"})
    except Exception as error:
        print(f"Error in clients.update: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.update method dropped an error: {error}"
        )

# DELETE ONE
def delete(id_client: int):
    try:
        with sqlite3.connect("SQL/database.db") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM clients WHERE id_client = ?;", (id_client,))
            client = cursor.fetchone()
        if client == None:
            return JSONResponse(status_code = 404, content = {"message":"Client not found"})
        else:
            cursor.execute("DELETE FROM clients WHERE id_client = ?;", (id_client,))
            cnxn.commit()
            return JSONResponse(status_code = 202, content = {"message":"Client deleted successfully"})
    except Exception as error:
        print(f"Error in clients.delete: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Model.delete method dropped an error: {error}"
        )
