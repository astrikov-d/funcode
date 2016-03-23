# FunCode

Install
-------
1. Clone this repository to your local machine.
2. `cd` to project root directory.
3. Install virtualenv: `virtualenv --no-site-packages --prompt="(funcode)" venv`
4. Install dependencies: `pip install -r ./requirements/base.txt`
5. Create user and database.
6. Run migrations: `python manage.py migrate`
7. Install fixtures: `python manage.py loaddata ./app/fixtures/users.json`
8. Run server: `python manage.py runsever`
9. Navigate your browser to http://127.0.0.1:8000

Testing
-------
To run tests you are just need to run `py.test`: `py.test --ds=conf.dev.settings ./tests`
