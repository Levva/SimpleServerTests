from test_serv import locators
from test_serv import some_func
import sys


def test_delete_user_1(find_random_user):
    id = find_random_user
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}')
    assert response_get_user == f'User with id={id} successfully deleted', f'Response is: "{response_get_user}"'


def test_delete_user_2(find_random_user):
    id = str(find_random_user)
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}')
    assert response_get_user == f'User with id={id} successfully deleted', f'Response is: "{response_get_user}"'


def test_delete_user_3():
    id = sys.maxsize
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}')
    assert response_get_user == f'User with id={id} not found', f'Response is: "{response_get_user}"'


def test_delete_user_4():
    id = 'id'
    response_get_user = dict(some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}'))
    assert response_get_user['detail'][0]['type'] == 'type_error.integer', f'Response is: "{response_get_user}"'


def test_delete_user_5():
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}')
    assert response_get_user == '1 required parameter are expected: id', f'Response is: "{response_get_user}"'


def test_delete_user_6(rename_users_file, find_random_user):
    id = find_random_user
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}')
    assert response_get_user == f'No users have been added yet', f'Response is: "{response_get_user}"'


def test_delete_user_7(locked_file, find_random_user):
    id = find_random_user
    response_get_user = some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}')
    assert response_get_user == f'User with id={id} successfully deleted', f'Response is: "{response_get_user}"'


def test_delete_user_8(find_random_user):
    id = find_random_user + 0.5
    response_get_user = dict(some_func.give_me_json(f'{locators.links.DELETE_USER}id={id}'))
    assert response_get_user['detail'][0]['type'] == 'type_error.integer', f'Response is: "{response_get_user}"'


if __name__ == "__main__":
    pass