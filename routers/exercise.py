from fastapi import APIRouter

from fastapi.responses import FileResponse

from csv import DictReader

router = APIRouter(prefix="/api/exercise")

def unpack_csv_file(csv_filepath):
    data = []
    with open(csv_filepath, 'r') as csvfile:
        some_reader = DictReader(csvfile)
        for row in some_reader:
            data.append(row)
    return data

@router.get("/user")
async def get_data_user(data_format="json"):
    filepath = "csvs/exercise/dummy-user-data.csv"
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-user-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return json_data

@router.get("/sensitive")
async def get_sensitive_user_data(data_format="json"):
    filepath = "csvs/exercise/dummy-sensitive-user-data.csv"
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-sensitive-user-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return json_data

@router.get("/transaction")
async def get_transaction_data(data_format="json"):
    filepath = "csvs/exercise/dummy-transaction-data.csv"
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-bank-account-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return json_data

@router.get("/ip-logs")
async def get_ip_data(data_format="json"):
    filepath = "csvs/exercise/dummy-ip-data.csv"
    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-ip-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return json_data