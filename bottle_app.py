
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run

@route('/')
def hello_world():
    return 'Hello World!'

application = default_app()
run(host='localhost', port=8080, debug=True)
