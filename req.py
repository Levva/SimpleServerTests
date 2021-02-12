import requests
import sys

#
#
# """
# Example of a request to add a user with name = TestName and surname = TestSurname:
# http://127.0.0.1:8000/edit?id=3&name=TestName&surname=TestSurname
# """
#
#
# r = requests.get('http://127.0.0.1:8000/add?name=TestName&surname=TestSurname')
# print(r.status_code)
# print(r.json())
#
#
# """
# Example of a search request for a user with id = 2:
# http://127.0.0.1:8000/get?id=2
# """
#
# r = requests.get(f'http://127.0.0.1:8000/get?id={sys.maxsize}')
# print(r.status_code)
# print(r.json())
#
#
# """
# An example of a request to update user with id = 3 for name = TestName and surname = TestSurname:
# http://127.0.0.1:8000/edit?id=3&name=TestName&surname=TestSurname
# """
#
#
# r = requests.get('http://127.0.0.1:8000/edit?id=3&name=TestName&surname=TestSurname')
# print(r.status_code)
# print(r.json())
#
#
# """
# An example of a request to delete user a user with id = 4:
# http://127.0.0.1:8000/delete?id=4
# """
#
# r = requests.get(f'http://127.0.0.1:8000/delete?id=4')
# print(r.status_code)
# print(r.json())
#
r = requests.post('http://127.0.0.1:8000/items/5',
                  json={"name": "string", "surname": "string", 'bool_value': 0})
print(r.status_code)
print(r.json())
