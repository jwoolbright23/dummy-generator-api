from fastapi import FastAPI

from routers import walkthrough

app = FastAPI()

app.include_router(walkthrough.router)