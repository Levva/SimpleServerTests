from test_serv import locators
from test_serv import some_func
import json
import sys


def test_get_user_1(add_user, find_random_user):
    id = find_random_user
    response_get_user = json.loads(some_func.give_me_json(f'{locators.links.GET_USER}id={id}'))
    print(response_get_user)
    assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'


def test_get_user_2(find_random_user):
    id = find_random_user
    try:
        response_get_user = json.loads(some_func.give_me_json(f'{locators.links.GET_USER}id={id}'))
        assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'
    except:
        response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
        assert response_get_user == f'Could not find user with id={id}', f'Response is: "{response_get_user}"'


def test_get_user_3():
    id = sys.maxsize
    response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
    assert response_get_user == f'Could not find user with id={id}', f'Response is: "{response_get_user}"'


def test_get_user_4():
    id = 0
    response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
    assert response_get_user == f'Could not find user with id={id}', f'Response is: "{response_get_user}"'


def test_get_user_5():
    response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}')
    assert response_get_user == '1 required parameter are expected: id', f'Response is: "{response_get_user}"'


def test_get_user_6():
    id = sys.maxsize + 1
    response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
    assert response_get_user == f'Could not find user with id={id}', f'Response is: "{response_get_user}"'


def test_get_user_7(find_random_user):
    id = str(find_random_user)
    response_get_user = json.loads(some_func.give_me_json(f'{locators.links.GET_USER}id={id}'))
    assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'


def test_get_user_8():
    id = 'id'
    try:
        response_get_user = json.loads(some_func.give_me_json(f'{locators.links.GET_USER}id={id}'))
        assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'
    except Exception as type:
        assert type.__class__ == TypeError, f'Exception is: "{type.__class__}"'


def test_get_user_9(rename_users_file, find_random_user):
    id = find_random_user
    response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
    assert response_get_user == f'No users have been added yet', f'Response is: "{response_get_user}"'


def test_get_user_10(locked_file, find_random_user):
    id = find_random_user
    try:
        response_get_user = some_func.give_me_json(f'{locators.links.GET_USER}id={id}')
        assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'
    except Exception as type:
        assert type.__class__ == PermissionError, f'Exception is: "{type.__class__}"'


def test_get_user_11(find_random_user):
    id = find_random_user + 0.5
    try:
        response_get_user = json.loads(some_func.give_me_json(f'{locators.links.GET_USER}id={id}'))
        assert len(response_get_user) > 0, f'Response is: "{response_get_user}"'
    except Exception as type:
        assert type.__class__ == TypeError, f'Exception is: "{type.__class__}"'


if __name__ == "__main__":
    pass