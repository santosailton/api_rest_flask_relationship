from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config_database import SQLALCHEMY_DATABASE_URI

from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.app_context().push()

from views.views import *

if __name__ == '__main__':
    app.run(host="127.0.0.1")
