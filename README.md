# BACKEND

## Requirements

- Postgres: 12.0
- Python: 3.8

## Instalations

- Create .env file using .env.example
- Change to ./backend directory
- Create virtual environment
  > `virtualenv --python=python3 ./env`
- Activate the environment
  > `source env/bin/activate`
- Install all requirements
  > `pip3 install -r requirements.txt`
- Prepare the database
  > `createdb database_name`
- Change the database url in alembic.ini file
- Run all migrations
  > `alembic upgrade head`
- Run the server
  > `python3 -m app.main`

## Alembic Commands

- Check for changes and generate migration script

  > `alembic revision --autogenerate -m "Some message describing the migration script"`

- Run latest migration script

  > `alembig upgrade head`
