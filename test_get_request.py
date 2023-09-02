import requests
import pandas as pd


def make_get_request(subs):
    url = f"http://localhost:8000/subtitles_level/?subs={subs}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    print('Send request to the server')
    print('Please, wait a few seconds...')

    df = pd.read_csv("../data/English_scores/movie_subs_level.csv")
    subs = df['subs'][22]

    response_data = make_get_request(subs)
    print(response_data)
