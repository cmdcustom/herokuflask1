import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'hi'

app.run(host='localhost', port=8080)
