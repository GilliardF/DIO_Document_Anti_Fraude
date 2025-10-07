import os 
from dotenv import load_env
load_env()

class Config:
    ENDPOINT=os.getenv("ENDPOINT")
    KEY=os.getenv("SUBSCRIPTION_KEY")
    AZURE_STORAGE_CONNECTION_STRING=os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME=os.getenv("CONTAINER-NAME")