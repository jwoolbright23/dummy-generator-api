from fastapi import FastAPI

from routers import walkthrough
from routers import exercise

app = FastAPI()

app.include_router(walkthrough.router)
app.include_router(exercise.router)