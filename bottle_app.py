import os

# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template, get, post, request

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()


@get('/')
@get('/todo-list')
def todo_list():
    return template("todo-list")

@get('/todo-list/<item_name>')
def todo_list_item(item_name):
    return template("todo-item", item_name=item_name)

@get('/todo-list/add-item')
def add_item_page():
    return template("add-item")

@post('/todo-list/add-item')
def add_item():
    new_item = request.forms.get("item_name").strip()
    print("added item: ", new_item)
    return template("todo-list")

if ON_PYTHONANYWHERE:
    application = default_app()
else:
    run(host='localhost', port=8080, debug=True)
