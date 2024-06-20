#!/usr/bin/python3
""" Script to obtain subscribers count from a subreddit """

from requests import get

def number_of_subscribers(subreddit):
    """ Function to get subscriber count """
    if subreddit and isinstance(subreddit, str):
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        try:
            response = get(url, headers=headers, allow_redirects=False)
            if response.status_code == 200:
                data = response.json()
                subscribers = data.get('data', {}).get('subscribers', 0)
                return subscribers
            else:
                return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    return 0

