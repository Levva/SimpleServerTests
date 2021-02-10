
from fastapi import FastAPI
import uvicorn
import json
import csv

class global_param:
    FILE = 'bs.csv'
    FIELDNAMES = ['id', 'name', 'surname']

'''
methods of server
'''


def csv_reader():
    result = []
    try:
        with open(global_param.FILE, "r") as csv_file:
            reader = tuple(csv.reader(csv_file))
        return reader
    except:
        return result


def csv_writer(some_data):
    try:
        with open(global_param.FILE, "a+") as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\r', fieldnames=global_param.FIELDNAMES)
            for row in some_data:
                if len(csv_reader()) == 0:
                    writer.writeheader()
                    row['id'] = 1
                else:
                    row['id'] = int(csv_reader()[-1][0]) + 1
                writer.writerow(row)
            csv_file.close()
        return True
    except:
        return False

def json_format(text):
    data = json.dumps(text)
    return data


def get_user(id):
    result = []
    list_of_user = csv_reader()
    if len(list_of_user) == 0:
        return 'No users have been added yet'
    else:
        list_of_user = list_of_user[1:]
    for row in list_of_user:
        if int(row[0]) == id:
            result.append([row[1], row[2]])
    if len(result) == 0:
        return f'Could not find user with id={id}'
    elif len(result) > 1:
        dict_res = {}
        for i in range(len(result)):
            dict_res[i] = result[i]
        return json_format(dict_res)
    else:
        return json_format(result)


def edit_user(id, name='', surname=''):

    list_of_user = csv_reader()

    if len(list_of_user) == 0:
        return 'No users have been added yet'
    else:
        list_of_user = list_of_user[1:]

    count = 0
    for row in list_of_user:
        if int(row[0]) == id:
            count +=1
            if name != '':
                row[1] = name
            if surname != '':
                row[2] = surname
    if count > 0:
        csv_update(list_of_user)
        return True
    else:
        return f'User with id={id} not found'


def delete_user(id):
    list_of_user = csv_reader()
    deleted_element = 0
    if len(list_of_user) == 0:
        return 'No users have been added yet'
    else:
        list_of_user = list_of_user[1:]
        count = 0
        for i in range(len(list_of_user)):
            if int(list_of_user[i][0]) == id:
                deleted_element = i
            else:
                count += 1
    if count != len(list_of_user):
        list_of_user.pop(deleted_element)
        csv_update(list_of_user)
        return True
    else:
        return f'User with id={id} not found'


def csv_update(some_data):
    try:
        with open(global_param.FILE, "w+") as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\r', fieldnames=global_param.FIELDNAMES)
            writer.writeheader()
            for row in some_data:
                dict_row = {'id': row[0], 'name': row[1], 'surname': row[2]}
                writer.writerow(dict_row)
        return True
    except:
        return False


app = FastAPI()


@app.get('/add')
def method(name: str = '', surname: str = ''):
    if not (name and surname):
        return '2 required parameters are expected: name and surname'
    some_data = [{'name': name, 'surname': surname}]
    add_status = csv_writer(some_data)
    if add_status:
        return f'User {name} {surname} successfully added'
    else:
        return 'Unable to access the user list'


@app.get('/get')
def method(id: int = 0):
    if not id:
        return '1 required parameter are expected: id'
    user_data = get_user(id)
    return user_data


@app.get('/edit')
def method(id: int, name='', surname=''):
    if not id:
        return '1 required parameter are expected: id'
    edit_status = edit_user(id, name, surname)
    if edit_status == True:
        return f'User with id={id} successfully edited'
    else:
        return edit_status


@app.get('/delete')
def method(id: int):
    if not id:
        return '1 required parameter are expected: id'
    delete_status = delete_user(id)
    if delete_status == True:
        return f'User with id={id} successfully deleted'
    else:
        return delete_status


@app.post('/')
def method():
    pass


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
