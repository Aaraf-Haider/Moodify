from flask import Flask, render_template, request, redirect, url_for
from models import db, Artist,Song
from sqlalchemy import inspect

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)




@app.route("/")
def index():
      with app.app_context():
        inspector = inspect(db.engine)  # ✅ Use SQLAlchemy Inspector
        tables = inspector.get_table_names()  # ✅ Correct way to list tables
        print("Existing tables in database:", tables)
        try:
            songs_data = db.session.query(Song).all()
            artists_data = db.session.query(Artist).all()
            print("Database connected successfully! ✅")
            print(f"Fetched {len(songs_data)} records from the table.")
            print(f"Fetched {len(artists_data)} records from the table.")
            return render_template("index.html", songs=songs_data, artists=artists_data)
        except Exception as e:
            print("Error connecting to database :", e)
            return "Database connection failed!"
    
        

@app.route("/happy")
def happy():
    with app.app_context():
        inspector = inspect(db.engine)  # ✅ Use SQLAlchemy Inspector
        tables = inspector.get_table_names()  # ✅ Correct way to list tables
        print("Existing tables in database:", tables)
        try:
            songs_data = db.session.query(Song).filter(Song.energy>=0.6,Song.tempo<=160,Song.tempo>=100).all()
            artists_data = db.session.query(Artist).all()
            print("Database connected successfully! ✅")
            print(f"Fetched {len(songs_data)} records from the table.")
            print(f"Fetched {len(artists_data)} records from the table.")
            return render_template("happy.html", songs=songs_data, artists=artists_data)
        except Exception as e:
            print("Error connecting to database :", e)
            return "Database connection failed!"

@app.route("/sad")
def sad():
    with app.app_context():
        inspector = inspect(db.engine)  # ✅ Use SQLAlchemy Inspector
        tables = inspector.get_table_names()  # ✅ Correct way to list tables
        print("Existing tables in database:", tables)
        try:
            songs_data = db.session.query(Song).filter(Song.energy<=0.6,Song.tempo<=119).all()
            artists_data = db.session.query(Artist).all()
            print("Database connected successfully! ✅")
            print(f"Fetched {len(songs_data)} records from the table.")
            print(f"Fetched {len(artists_data)} records from the table.")
            return render_template("sad.html", songs=songs_data, artists=artists_data)
        except Exception as e:
            print("Error connecting to database :", e)
            return "Database connection failed!"

@app.route("/energetic")
def energetic():
    with app.app_context():
        inspector = inspect(db.engine)  # ✅ Use SQLAlchemy Inspector
        tables = inspector.get_table_names()  # ✅ Correct way to list tables
        print("Existing tables in database:", tables)
        try:
            songs_data = db.session.query(Song).filter(Song.energy>=0.7,Song.tempo>=120).all()
            artists_data = db.session.query(Artist).all()
            print("Database connected successfully! ✅")
            print(f"Fetched {len(songs_data)} records from the table.")
            print(f"Fetched {len(artists_data)} records from the table.")
            return render_template("energetic.html", songs=songs_data, artists=artists_data)
        except Exception as e:
            print("Error connecting to database :", e)
            return "Database connection failed!"

@app.route("/chill")
def chill():
    with app.app_context():
        inspector = inspect(db.engine)  # ✅ Use SQLAlchemy Inspector
        tables = inspector.get_table_names()  # ✅ Correct way to list tables
        print("Existing tables in database:", tables)
        try:
            songs_data = db.session.query(Song).filter(Song.energy<=0.6,Song.tempo<=120, Song.tempo>50).all()
            artists_data = db.session.query(Artist).all()
            print("Database connected successfully! ✅")
            print(f"Fetched {len(songs_data)} records from the table.")
            print(f"Fetched {len(artists_data)} records from the table.")
            return render_template("chill.html", songs=songs_data, artists=artists_data)
        except Exception as e:
            print("Error connecting to database :", e)
            return "Database connection failed!"
        
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

if __name__ == "__main__":
    app.run(debug=True)




'''''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/PMLS/Desktop/mood_music_recommender/music_recommender.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Artist {self.name}>'

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    ##mood = db.Column(db.String(50), nullable=False)  # Add mood column
    artist = db.relationship('Artist', backref='songs')

    def __repr__(self):
        return f'<Song {self.name} by {self.artist.name}>'
'''