# FunCode

Install
-------
1. Clone this repository to your local machine.
2. Install virtualenv: `virtualenv --no-site-packages --prompt="(funcode)" venv`
3. Install dependencies: `pip install -r ./requirements/base.txt`
4. Create user and database.
5. Run migrations: `python manage.py migrate`
6. Install fixtures: `python manage.py loaddata ./app/fixtures/users.json`
7. Run server: `python manage.py runsever`
8. Navigate your browser to http://127.0.0.1

Testing
-------
To run tests you are just need to run `py.test`: `py.test ./tests`
