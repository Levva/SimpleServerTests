from pydantic import BaseModel
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
            users_state = csv_reader()
            for row in some_data:
                if len(users_state) == 0:
                    row['id'] = 1
                    writer.writeheader()
                elif len(users_state) == 1:
                    row['id'] = 1
                else:
                    row['id'] = int(users_state[-1][0]) + 1
                writer.writerow(row)
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
        return {'warning': 'No users have been added yet'}
    else:
        list_of_user = list_of_user[1:]
    for row in list_of_user:
        if int(row[0]) == id:
            result.append([row[1], row[2]])
    if len(result) == 0:
        return {'error': f'User with id={id} not found'}
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
        return {'warning': 'No users have been added yet'}
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
        return {'error': f'User with id={id} not found'}


def delete_user(id):
    list_of_user = csv_reader()
    deleted_element = 0
    if len(list_of_user) == 0:
        return {'warning': 'No users have been added yet'}
    else:
        list_of_user = list(list_of_user[1:])
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
        return {'error': f'User with id={id} not found'}


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


class Item(BaseModel):
    name: str = ''
    surname: str = ''
    id: int = 0


@app.post("/add")
def method(item: Item):
    if not (item.name or item.surname):
        return {'error': '2 required parameters are expected: name and surname'}
    some_data = [{"name": item.name, "surname": item.surname}]
    add_status = csv_writer(some_data)
    if add_status:
        return {'status': f'User {item.name} {item.surname} successfully added'}
    else:
        return {'error': 'Unable to access the user list'}


@app.get('/get')
def method(id: int = 0):
    if not id:
        return '1 required parameter are expected: id'
    user_data = get_user(id)
    return user_data


@app.put('/edit/{id}')
def method(id: int, item: Item):
    if id == 0:
        return {'error': 'ID must be more then 0'}
    edit_status = edit_user(id, item.name, item.surname)
    if edit_status == True:
        return {'status': f'User with id={id} successfully edited'}
    else:
        return edit_status


@app.put('/edit')
def method(item: Item):
    if item.id == 0:
        return {'error': 'ID must be more then 0'}
    edit_status = edit_user(item.id, item.name, item.surname)
    if edit_status == True:
        return {'status': f'User with id={item.id} successfully edited'}
    else:
        return edit_status


@app.delete('/delete/{id}')
def method(id: int):
    if id == 0:
        return {'error': 'ID must be more then 0'}
    delete_status = delete_user(id)
    if delete_status == True:
        return {'status': f'User with id={id} successfully deleted'}
    else:
        return delete_status


@app.delete('/delete')
def method(item: Item):
    if item.id == 0:
        return {'error': 'ID must be more then 0'}
    delete_status = delete_user(item.id)
    if delete_status == True:
        return {'status': f'User with id={item.id} successfully deleted'}
    else:
        return delete_status


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')
