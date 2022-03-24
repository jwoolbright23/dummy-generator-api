# Need multiple get requests

# Create new data and return it

# End point for dummy data we created: User data, sensitive user data, bank account data, ip data

'''
- GET /data/user -> CSV File
- GET /data/user/sensitive
- GET /data/transaction
- GET /data/ip-logs
'''


from fastapi import FastAPI
from fastapi.responses import FileResponse
import csv

app = FastAPI()


@app.get("/")
async def root():
    return {"csv": "John Matthews, superUser, pw: safelyregistered, email: whoknows@email.com"}

'''
GET /data/user -> CSV file
GET /data/user?type=json -> JSON representation of the CSV file
'''

@app.get("/data/user")
async def get_data_user(data_format="json"):
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse("dummy-user-data1.csv", filename="random-user-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = []
    with open('dummy-user-data1.csv', 'r') as csvfile:
            some_reader = csv.DictReader(csvfile)
            for row in some_reader:
                json_data.append(row)
    return json_data

@app.get("/data/user/sensitive")
async def get_sensitive_user_data(data_format="json"):
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse("dummy-sensitive-user-data.csv", filename="random-sensitive-user-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = []
    with open("dummy-sensitive-user-data.csv", 'r') as csvfile:
            some_reader = csv.DictReader(csvfile)
            for row in some_reader:
                json_data.append(row)
    return json_data

@app.get("/data/transaction")
async def get_transaction_data(data_format="json"):
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse("dummy-bank-account-data.csv", filename="random-bank-account-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = []
    with open('dummy-bank-account-data.csv', 'r') as csvfile:
            some_reader = csv.DictReader(csvfile)
            for row in some_reader:
                json_data.append(row)
    return json_data

@app.get("/data/ip-logs")
async def get_ip_data(data_format="json"):
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse("dummy-ip-data.csv", filename="random-ip-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = []
    with open('dummy-ip-data.csv', 'r') as csvfile:
            some_reader = csv.DictReader(csvfile)
            for row in some_reader:
                json_data.append(row)
    return json_data