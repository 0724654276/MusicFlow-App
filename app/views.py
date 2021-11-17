from flask import render_template
from app import app
from app.request import get_music


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular music
    popular_music = get_music('popular')
    print(popular_music)
    title = 'Home - Welcome to The best Music Review Website Online'
    return render_template('index.html', title = title,popular = popular_music)
@app.route('/music/<int:music_id>')
def music(music_id):

    '''
    View music page function that returns the music details page and its data
    '''
    return render_template('music.html',id = music_id)