from app import app
import urllib.request,json
from .models import Music

# Getting api key
api_key = app.config['MUSIC_API_KEY']


# Getting the movie base url
base_url = app.config["MUSIC_API_BASE_URL"]

def get_music(category):
    '''
    Function that gets the json response to our url request
    '''
    get_music_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_music_url) as url:
        get_music_data = url.read()
        get_music_response = json.loads(get_music_data)

        music_results = None

        if get_music_response['results']:
            music_results_list = get_music_response['results']
            music_results = process_results(music_results_list)


    return music_results
def process_results(music_list):
    '''
    Function  that processes the music result and transform them to a list of Objects

    Args:
        music_list: A list of dictionaries that contain music details

    Returns :
        music_results: A list of music objects
    '''
    music_results = []
    for music_item in music_list:
        id = music_item.get('id')
        title = music_item.get('original_title')
        overview = music_item.get('overview')
        poster = music_item.get('poster_path')
        vote_average = music_item.get('vote_average')
        vote_count = music_item.get('vote_count')

        if poster:
            music_object = Music(id,title,overview,poster,vote_average,vote_count)
            music_results.append(music_object)

    return music_results
   
