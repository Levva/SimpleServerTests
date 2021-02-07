import requests
import json


def give_me_json(link):
    try:
        response = requests.get(link)
        return json.loads(response.text)
    except:
        f'OPS! URL {link} not available. Please try again and maybe you will be lucky now'