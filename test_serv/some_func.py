from serv import global_param
import requests
import csv


def give_me_json(link):
    try:
        response = requests.get(link)
        print(response.json())
        return response.json(), response.status_code
    except:
        f'OPS! URL {link} not available. Please try again and maybe you will be lucky now'


def get_last_user():
    try:
        with open(f'{global_param.FILE}', 'r') as csv_file:
            list_of_user = tuple(csv.reader(csv_file))
            return list_of_user[-1]
    except:
        f"Can't open file {global_param.FILE}"
