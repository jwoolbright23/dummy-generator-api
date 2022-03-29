from fastapi import APIRouter

from fastapi.responses import FileResponse

from csv import DictReader

from lc_pydatagenerator.generate_random import user_data

router = APIRouter(prefix="/api/random")

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

    # guard clause 1 (provided query parameter data_format=csv)
    if data_format == "csv":
        return FileResponse(filepath, filename="random-user-data.csv")
    
    # default behavior of endpoint (no options: query parameters, path variable, request body)
    json_data = unpack_csv_file(filepath)

    return json_data