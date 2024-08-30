import os

import requests


def get_image_from_api() -> list[str]:
    """get image from thecatapi.com"""
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': os.getenv('API_KEY', 'DEMO_API_KEY')
    }
    params = {
        'limit': os.getenv('CATS_ON_PAGE', 10),
    }
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url, headers=headers, params=params).json()
    return [image['url'] for image in response]
