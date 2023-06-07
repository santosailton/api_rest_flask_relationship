from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config_database import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
app.app_context().push()

from views.views import *

if __name__ == '__main__':
    app.run(host="127.0.0.1")
