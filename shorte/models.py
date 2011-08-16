from shorte import app
from flaskext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/shorte.db'
db = SQLAlchemy(app)

class Shorte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(20), unique=True)
    long_url = db.Column(db.String(255), unique=True)
    hits = db.Column(db.Integer)

    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url
