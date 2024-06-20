# 0-subs.py

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("Response Status Code: {}".format(response.status_code))  # Debug print
        if response.status_code == 200:
            data = response.json()
            print("Response JSON Data: {}".format(data))  # Debug print
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        elif response.status_code == 404:
            print("Subreddit not found (404).")  # Debug print
            return 0
        else:
            print("Unexpected status code: {}".format(response.status_code))  # Debug print
    except requests.RequestException as e:
        print("An error occurred: {}".format(e))
        return 0
    return 0

