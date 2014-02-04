# Flask-Restful-TODO [![Build Status](https://travis-ci.org/erkarl/flask-restful-todo.png?branch=master)](https://travis-ci.org/erkarl/flask-restful-todo)

Yet another simple TODO app API created with [flask-restful](https://github.com/twilio/flask-restful). Working demo deployed to Heroku available at [todo-api.karlranna.com](http://todo-api.karlranna.com)

Frontend repository available at [ember-todos](https://github.com/erkarl/ember-todos).

## Install

Clone this repo, set up and activate a virtualenv and install the required python dependencies
```console
git clone git@github.com:erkarl/flask-restful-todo.git
cd flask-restful-todo 
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Create the database
```console
make db
```

## Run the server 
```console
make server
```

## Tests 
```console
make test 
```
