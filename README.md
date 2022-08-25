# FlaskExamProject




-----Technologies used-----

Python3 - A programming language that lets you work more quickly (The universe loves speed!).
Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
Virtualenv - A tool to create isolated virtual environments
PostgreSQL – Postgres database offers many advantages over others.
SQLAlchemy - is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL
Minor dependencies can be found in the requirements.txt file on the root folder.


-----Installation dependencies-----

Install with pip:
$ pip install -r requirements.txt

-----Flask Application Structure-----


│   .env 
│   .gitignore 
│   config.py 
│   db.py>
│   main.py
│   requirements.txt
│       
├───managers
│   │   auth.py
│   │   employee.py
│   │   store.py
│   │   store_user.py
│   │   task.py
│   │   __init__.py
│           
├───migrations
│   │   alembic.ini
│   │   env.py
│   │   README
│   │   script.py.mako
│   │   
│   ├───versions
│   │   │   1939751e203b_.py
│   │   │   5e2793b346f3_add_transaction_table.py
│   │   │   665c3735b4eb_.py
│   │   │   7772fbeced75_edit_create_and_update_field.py
│   │   │   81d384d9e8fa_edit_create_and_update_field.py
│   │   │   c6d0eea48485_edit_create_and_update_field.py
│   │   │   c969fd225319_.py
│   │   │   e1a77fc7ceb2_.py
│   │   │   e2c877a4e410_initial_migration.py
│   │   │   f7a584397b3e_.py
│   │   │   f9593d97d255_rename_employ_comment_to_employee_.py
│           
├───models
│   │   enums.py
│   │   store.py
│   │   tasks.py
│   │   transaction.py
│   │   user.py
│   │   __init__.py
│   │   
├───resources
│   │   auth.py
│   │   routes.py
│   │   __init__.py
│   │   
│           
├───schemas
│   │   __init__.py
│   │   
│   ├───requests
│   │   │   auth.py
│   │   │   base.py
│   │   │   __init__.py
│   │   │   
│   │           
│   ├───responses
│   │   │   task.py
│   │   │   __init__.py
│   │   │   
│   │           
├───services
│   │   wise.py
│   │   __init__.py
│   │   
├───tests
│   │   app_test.py
│   │   factories.py
│   │   helpers.py
│   │   __init__.py
│   │   
│   └───.pytest_cache
│       │   .gitignore
│       │   CACHEDIR.TAG
│       │   README.md
│       │   
│                   
├───utils
│   │   decorators.py
│   │   __init__.py
│   │   


-----Usage-----

Users endpoint:

1. Register Employees: POST http://127.0.0.1:5000/register-employees/    -Authorization: needed, Content-Type: application/json

REQUEST:
{"first_name": "test", "last_name": "test", "password": "pass", "email": "test@test.bg","phone": "12345632178973","iban": "IE64IRCE92050112345673", "role": "employee"}

RESPONSE:
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI0LCJleHAiOjE2NjExNzEwMjJ9.XAg9bM909Y1pf1dpI9kawhHrg_yhGSA3uP8SeTIM9X4"
}

2. Register normal user: POST http://127.0.0.1:5000/register/    -Content-Type: application/json

REQUEST:

{"first_name": "test", "last_name": "test", "password": "pass", "email": "t@t.bg","phone": "12345678912345","nickname": "test",
"address": "testtest 23"}

RESPONSE:
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY2MTE3MTIwM30.XrSa4xfPhW9zLcBIVMeLJwVirkkjl7C6GSn_CKtA5sQ"
}

3. Login for Employee: POST http://127.0.0.1:5000/loginEmployee/  -Content-Type: application/json

REQUEST:

{"email": "t@t.com", "password": "pass"}

RESPONSE:
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY2MTE3MTIwM30.XrSa4xfPhW9zLcBIVMeLJwVirkkjl7C6GSn_CKtA5sQ"
}

4. Login for user: POST http://127.0.0.1:5000/login/  -Content-Type: application/json

REQUEST:

{"email": "t@t.com", "password": "pass"}

RESPONSE:
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY2MTE3MTIwM30.XrSa4xfPhW9zLcBIVMeLJwVirkkjl7C6GSn_CKtA5sQ"
}

5. Create task: POST http://127.0.0.1:5000/tasks/   -Authorization: needed, Content-Type: application/json

REQUEST:

{"task_name": "sometask", "description": "go to", "employee_id": 21}

RESPONSE:

"Task sometask number 72 assigned to employee employee"

6. Create items in store: POST http://127.0.0.1:5000/items/   -Authorization: needed, Content-Type: application/json

REQUEST:

{"item_name": "fork", "serial_number": "GE044005", "quantity": 10, "delivery_price": 5}

RESPONSE:

"added item fork with quantity 10"

7. Get items in store: GET http://127.0.0.1:5000/items/ -Authorization: needed, Content-Type: application/json

REQUEST:



RESPONSE:

[
    {
        "delivery_price": 5,
        "serial_number": "GE044005",
        "id": 44,
        "item_name": "knife",
        "dealer_price": 7,
        "sell_price": 9,
        "quantity": 10
    },
    {
        "delivery_price": 5,
        "serial_number": "GE044005",
        "id": 45,
        "item_name": "fork",
        "dealer_price": 7,
        "sell_price": 9,
        "quantity": 30
    }
]

8. Delete items from store: DELETE http://127.0.0.1:5000/item/44 -Authorization: needed, Content-Type: application/json

REQUEST:

{"id": 44}   #Enter Item ID

RESPONSE:

HTTP status code 204 OK, 404 Not Found

9. Get task, depends of logged employee: GET http://127.0.0.1:5000/tasks/ -Authorization: needed, Content-Type: application/json

REQUEST:



RESPONSE:

[
    {
        "id": 72,
        "state": "In Progress",
        "employee_id": 21,
        "employee_comments": "Add comment:",
        "task_name": "sometask",
        "used_parts": "Not used",
        "description": "go to"
    },
    {
        "id": 73,
        "state": "In Progress",
        "employee_id": 22,
        "employee_comments": "Add comment:",
        "task_name": "sometask",
        "used_parts": "Not used",
        "description": "go to"
    },
    {
        "id": 74,
        "state": "In Progress",
        "employee_id": 22,
        "employee_comments": "Add comment:",
        "task_name": "sometask",
        "used_parts": "Not used",
        "description": "go to"
    },

]


10. Updtate task: PUT http://127.0.0.1:5000/task/72  -Authorization: needed, Content-Type: application/json

REQUEST:

{"id": 72,"used_parts": "Ne sa izpolzvani", "employee_comments": "comment", "state":"done"}

RESPONSE:

HTTP status code 204 OK, 404 Not Found

11. Delete task: DELETE http://127.0.0.1:5000/task/73 -Authorization: needed, Content-Type: application/json

REQUEST:

{"id": 73}  #TASK ID

RESPONSE:

HTTP status code 204 OK, 404 Not Found

12. Buying items from store: POST http://127.0.0.1:5000/items/buy/ -Content-Type: application/json

REQUEST:

{"id":44, "quantity": 10}

RESPONSE:

"u bought 10 knife"

13. Employee payment salary:  POST http://127.0.0.1:5000/salary/5/payment/ -Authorization: needed, Content-Type: application/json
REQUEST:

{"id":20} #Enter employee ID

RESPONSE:

"U paid 354.0 to admin admin"

14. Update employee salary PUT http://127.0.0.1:5000/salary/5/update/ -Authorization: needed, Content-Type: application/json
REQUEST:

{"id": 20, "salary": 354}   #Enter employee ID

RESPONSE:

" admin admin salary change to 354 "
