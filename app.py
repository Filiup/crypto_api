from flask import Flask
from app_container import AppContainer
from dotenv import load_dotenv

from crypto.crypto_controller import *

load_dotenv()

def create_app() -> Flask:
    app_container = AppContainer()
    app_container.wire(modules=[__name__])

    app = Flask(__name__)
    app.register_blueprint(crypto_blueprint)
    return app