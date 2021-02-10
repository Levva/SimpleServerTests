import requests
import json


def give_me_json(link):
    try:
        response = requests.get(link, timeout=(5, 10))
        return response.json(), response.status_code
    except:
        f'OPS! URL {link} not available. Please try again and maybe you will be lucky now'