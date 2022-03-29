from fastapi import APIRouter

from fastapi.responses import FileResponse, JSONResponse

from csv import DictReader

from lc_pydatagenerator.generate_random import user_data

from os import remove

from starlette.background import BackgroundTask

router = APIRouter(prefix="/api/random")

def remove_file(path):
    remove(path)

def unpack_csv_file(csv_filepath):
    data = []
    with open(csv_filepath, 'r') as csvfile:
        some_reader = DictReader(csvfile)
        for row in some_reader:
            data.append(row)
    return data

@router.get("/user")
async def get_data_user(data_format="json"):

    filepath = "csvs/random/random-dummy-user-data.csv"

    user_data(filepath, 1000)
    
    task = BackgroundTask(remove_file, path=filepath)

    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-user-data.csv", background=task)
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return JSONResponse(content=json_data, background = task)