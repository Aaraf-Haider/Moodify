from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\PMLS\Desktop\mood_music_recommender\music_recommender.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Reflect existing tables within the application context
with app.app_context():
    db.Model.metadata.reflect(db.engine)

# Define a dynamic model for an existing table
class Song(db.Model):
    __table__ = db.Model.metadata.tables['songs']

class Artist(db.Model):
    __table__ = db.Model.metadata.tables['artists']