from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import create_app
from db import db

app = create_app()


if __name__ == "__main__":
    app.run()
