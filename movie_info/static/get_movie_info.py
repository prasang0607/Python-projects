import json, requests

def movie_info(name):
    url = r"https://www.omdbapi.com/?apikey=9276b87c&t="+name
    raw_data = requests.get(url)
    json_data = json.loads(raw_data.text)
    if json_data['Response'] == 'True':
        return json_data
    else:
        return 'No data found'
