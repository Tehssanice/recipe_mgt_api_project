from fastapi import FastAPI

from routes import app

api = FastAPI(title="Recipe Management API")

api.include_router(app, prefix="/api")
