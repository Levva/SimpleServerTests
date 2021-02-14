import requests

"""
Example of a request to add a user with name = TestName and surname = TestSurname:
"""

r = requests.post('http://127.0.0.1:8000/add',
                  json={'name': "TestName", 'surname': "TestSurname"})
print(r.status_code)
print(r.json())

"""
Example of a search request for a user with id = 2:
"""

r = requests.get(f'http://127.0.0.1:8000/get?id=2')
print(r.status_code)
print(r.json())

"""
An example of a request to update user with id = 3 for name = TestName and surname = TestSurname:
"""

r = requests.put('http://127.0.0.1:8000/edit/3',
                 json={'name': "TestName", 'surname': "TestSurname"})
print(r.status_code)
print(r.json())

r = requests.put('http://127.0.0.1:8000/edit',
                 json={'id': 3, 'name': "TestName", 'surname': "TestSurname"})
print(r.status_code)
print(r.json())

"""
An example of a request to delete user a user with id = 4:
"""

r = requests.delete('http://127.0.0.1:8000/delete/4')
print(r.status_code)
print(r.json())

r = requests.delete('http://127.0.0.1:8000/delete',
                    json={'id': 4})
print(r.status_code)
print(r.json())
