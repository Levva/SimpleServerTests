from test_serv import locators
from test_serv import some_func
import json
import sys


def test_update_user_1(add_user, find_random_user):
    id = find_random_user
    name = 'test name 1'
    surname = 'test surname 1'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                          f'&name={name}&surname={surname}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_2(add_user, find_random_user):
    id = find_random_user
    name = 'test name 2'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}&name={name}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_3(add_user, find_random_user):
    id = find_random_user
    surname = 'test surname 3'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}&surname={surname}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_4(add_user, find_random_user):
    id = find_random_user
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_5(add_user):
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}')
    assert response_get_user == f'1 required parameter are expected: id', f'Response is: "{response_get_user}"'


def test_update_user_6(add_user):
    id = sys.maxsize
    name = 'test name 6'
    surname = 'test surname 6'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                          f'&name={name}&surname={surname}')
    assert response_get_user == f'User with id={id} not found', f'Response is: "{response_get_user}"'


def test_update_user_7(add_user, find_random_user):
    id = str(find_random_user)
    name = 'test name 7'
    surname = 'test surname 7'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                          f'&name={name}&surname={surname}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_8(add_user):
    id = 'id'
    name = 'test name 8'
    surname = 'test surname 8'
    try:
        response_get_user = json.loads(some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                              f'&name={name}&surname={surname}'))
    except Exception as type:
        assert type.__class__ == TypeError, f'Exception is: "{type.__class__}"'


def test_update_user_9(rename_users_file, find_random_user):
    id = find_random_user
    name = 'test name 9'
    surname = 'test surname 9'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                          f'&name={name}&surname={surname}')
    assert response_get_user == f'No users have been added yet', f'Response is: "{response_get_user}"'


def test_update_user_10(locked_file, find_random_user):
    id = find_random_user
    name = 'test name 10'
    surname = 'test surname 10'
    response_get_user = some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                          f'&name={name}&surname={surname}')
    assert response_get_user == f'User with id={id} successfully edited', f'Response is: "{response_get_user}"'


def test_update_user_11(add_user, find_random_user):
    id = find_random_user + 0.5
    name = 'test name 8'
    surname = 'test surname 8'
    try:
        response_get_user = json.loads(some_func.give_me_json(f'{locators.links.UPDATE_USER}id={id}'
                                                              f'&name={name}&surname={surname}'))
    except Exception as type:
        assert type.__class__ == TypeError, f'Exception is: "{type.__class__}"'


if __name__ == "__main__":
    pass