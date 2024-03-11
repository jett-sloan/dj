from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db,PlayList,Song
from forms import AddPlayList, AddSong

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///play'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "sammydog"
connect_db(app)


@app.route('/')
def show_new_playlist():
    playlists = PlayList.query.all()
    return render_template('home.html', playlists=playlists)

@app.route("/add", methods=['GET','POST'])
def view_AddSong():
    form = AddPlayList()
    if form.validate_on_submit():
        play_list = PlayList(name=form.name.data, description=form.description.data)
        db.session.add(play_list)
        db.session.commit()
        return redirect('/')
    return render_template('add_playlist.html', form=form)



#see songs in playlist
    

@app.route('/add/<int:playlist_id>', methods=["GET", "POST"])
def add_song(playlist_id):
    playlist = PlayList.query.get_or_404(playlist_id)
    
    form = AddSong(obj=playlist)

    if form.validate_on_submit():
        new_song = Song(title=form.title.data, artist=form.artist.data)
        playlist.songs.append(new_song)
        db.session.add(new_song)
        db.session.commit()
        return redirect(f'/add/{playlist_id}')
    else:
        return render_template('playlist_id.html', form=form, playlist=playlist)

    
