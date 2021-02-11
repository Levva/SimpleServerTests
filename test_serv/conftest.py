import pytest
import requests
import os
import sys
import csv
from test_serv import locators
from serv import global_param


@pytest.fixture(scope='function')
def locked_file():
    file = open(global_param.FILE, 'a')
    print("Lock acquired")
    yield file
    file.close()


@pytest.fixture(scope='function')
def add_user():
    requests.get(f'{locators.links.ADD_USER}name=test&surname=test')


@pytest.fixture(scope='function')
def rename_users_file():
    if os.path.exists(global_param.FILE):
        os.rename(global_param.FILE, f'temp_{global_param.FILE}')
        yield
        os.rename(f'temp_{global_param.FILE}', global_param.FILE)
    else:
        yield


@pytest.fixture(scope='function')
def find_random_user():
    import random
    with open(f'{global_param.FILE}', 'r') as csv_file:
        list_of_user = random.choice(list(csv.reader(csv_file)))
    return random.choice(list_of_user[0])


if __name__ == "__main__":
    pass