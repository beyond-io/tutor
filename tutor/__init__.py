from flask import Flask  
from tutor.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__) 
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
