# Simpe srver

Для запуска использовать файл
serv.py

**Поддерживаются следующие действия:**

*Добавить пользователя:*

POST http://127.0.0.1:8000/add
{
name = "Name",
surname = "Surname"
}

name и surname - обязательные параметры

*Найти пользователя по id:*

GET http://127.0.0.1:8000/get?id={id}

где id - целое число > 0, обязательный параметр

*Изменить пользователя:*

PUT http://127.0.0.1:8000/edit/{id}
{
name = "Name",
surname = "Surname"
}

PUT http://127.0.0.1:8000/edit
{
name = "Name",
surname = "Surname",
id = N
}

где id - целое число > 0, обязательный параметр

*Удалить пользователя:*

DELETE http://127.0.0.1:8000/delete/{id}

DELETE http://127.0.0.1:8000/delete
{
id = N
}

где id - целое число > 0, обязательный параметр

Примеры запросов можно посмотреть в файле
req.py

