from fastapi import FastAPI

from routers import walkthrough
from routers import exercise
from routers import random

app = FastAPI()

app.include_router(walkthrough.router)
app.include_router(exercise.router)
app.include_router(random.router)