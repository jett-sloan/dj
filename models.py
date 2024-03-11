from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()


PlayListSong = db.Table(
    "play_list_songs",
    db.Column('play_list_id', db.Integer, db.ForeignKey('play_lists.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id'))
)



class PlayList(db.Model):

    __tablename__ = "play_lists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.Text, nullable=False)
    songs = db.relationship('Song', secondary=PlayListSong, backref='playlists', lazy='dynamic')



class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    artist = db.Column(db.String(200),nullable=False)