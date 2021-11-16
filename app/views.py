from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
@app.route('/music/<int:music_id>')
def music(music_id):

    '''
    View music page function that returns the music details page and its data
    '''
    return render_template('music.html',id = music_id)