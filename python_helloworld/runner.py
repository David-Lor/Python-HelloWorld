import uvicorn
from .app import app
from .settings import api_settings


def run():
    uvicorn.run(app, host=str(api_settings.host), port=api_settings.port)
