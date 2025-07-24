from fastapi import FastAPI
from fastapi.openapi.utils import status_code_ranges
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

#1
@app.get("/hello")
def read_hello(req:Request):
    accept_headers = req.headers.get("Accept")
    if accept_headers != "text/plain":
        return JSONResponse({"message": "Unsupported"}, status_code=400)
    return JSONResponse(content="Hello world",status_code=200)

#2
class WelcomeName(BaseModel):
    name: str
@app.get("/welcome")
def read_welcome(req:Request):
    return JSONResponse({"message": f"welcome {req.name}"},status_code=200)

#3
class StudentInfo (BaseModel):
    Reference : str
    FirstName : str
    LastName : str
    Age : int
@app.post("/students")
def read_students (request:StudentInfo):
    return {f"{request.Reference, request.FirstName, request.LastName, request.Age}"}

# 4
@app.get("/students")
def read_students_info():
    return JSONResponse(read_students , status_code=200)

#5
# Q5 : Créer une requête idempotente à travers une nouvelle route PUT /students, en utilisant
# l’attribut “Reference” comme identifiant unique. Autrement dit, si la Reference fournie dans le
# corps existe déjà, alors effectuer une modification si les valeurs ont été modifiées, sinon
# effectuer un ajout. (4 points)

