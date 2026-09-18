# split expenses

Django expense-sharing project with group models, expense CRUD views, server-rendered forms, and Docker configuration.

## Run locally

Create a Python virtual environment and install the checked-in requirements. Review the Django settings before applying migrations to a development database.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python splitexpense/manage.py migrate
python splitexpense/manage.py runserver
```

## Source guide

- [splitexpense/manage.py](splitexpense/manage.py)
