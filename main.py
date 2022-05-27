from fastapi import FastAPI

from routers import walkthrough
from routers import exercise
from routers import random

app = FastAPI(title="Random Data Generator", description="This random data generator was created for students going through the Linux curriculum located here - launchcodetechnicaltraining.org/linux", openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="/api/redoc")

app.include_router(walkthrough.router)
app.include_router(exercise.router)
app.include_router(random.router)
