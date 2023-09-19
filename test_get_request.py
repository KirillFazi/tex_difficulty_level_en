import requests
import pandas as pd


def make_get_request(subs):
    url = f"http://0.0.0.0:8000/subtitle_level/?subs={subs}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    df = pd.read_csv("data/movie_subs_level.csv")

    # for i in range(0, len(df), 2):
    #
    #     print('Send request to the server')
    #     print('Please, wait a few seconds...')
    #
    #     subs = str(df['subs'][i])[:45_000]
    #
    #     response_data = make_get_request(subs)
    #     print(response_data)

    print('Send request to the server')
    print('Please, wait a few seconds...')

    subs = str(df['subs'][1])[:40_000]

    response_data = make_get_request(subs)
    print(response_data)
