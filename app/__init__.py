from flask import Flask
from config import Config
#database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#login
from flask_login import LoginManager

#app and config
app = Flask(__name__)
app.config.from_object(Config)

#database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#login
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors