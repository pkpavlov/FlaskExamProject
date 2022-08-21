# FlaskExamProject




-----Technologies used-----

Python3 - A programming language that lets you work more quickly (The universe loves speed!).
Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
Virtualenv - A tool to create isolated virtual environments
PostgreSQL – Postgres database offers many advantages over others.
SQLAlchemy - is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL
Minor dependencies can be found in the requirements.txt file on the root folder.


-----Installation-----

Install with pip:
$ pip install -r requirements.txt

-----Flask Application Structure-----


│   .env
│   .gitignore
│   config.py
│   db.py
│   main.py
│   
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
