import pytest
import requests
import os
import sys
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
    for i in range(1, sys.maxsize):
        response = requests.get(f'{locators.links.GET_USER}id={i}')
        if response.text != f'"Could not find user with id={i}"':
            return i
        else:
            i += 1

if __name__ == "__main__":
    pass