from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

app.config['SECRET_KEY'] = '15efda52ac348a4f1c70d30d'

db=SQLAlchemy(app)


from market import routes