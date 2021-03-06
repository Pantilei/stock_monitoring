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

# Frontend

## Set up Eslint with Airbnb Style Guide

- Install Eslint
  > `yarn add eslint --save-dev`
- Installing the style guide
  > `yarn add eslint-config-airbnb --save-dev`
- List all the peer dependencies
  > `yarn info “eslint-config-airbnb@latest" peerDependencies`
- Either install the peer dependencies one after the other or use this shortcut if you have npm version 5+
  > `npx install-peerdeps --dev eslint-config-airbnb`
- Configure Eslint
  > Create configuration file `.eslintrc.js` and make sure to have `"extends": "airbnb"` in it
- Install Prettier
  > `yarn add --save-dev --save-exact prettier`
- Create `.prettierrc.js` file

## Create React Typescript project

> `npx create-react-app my-app --template typescript`

## Start Frontend server

> `yarn start`
