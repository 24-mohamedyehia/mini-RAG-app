from fastapi import FastAPI     # import FastAPI class from fastapi package
from routes import base     # this is the file we created
from dotenv import load_dotenv    # this package is used to load environment variables from .env file
load_dotenv(".env")

app = FastAPI()

app.include_router(base.base_router)