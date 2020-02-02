from flask import Flask
from flask import jsonify
import wikipedia


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/bob')
def bob():
    val = {"value": "bob"}
    return jsonify(val)

@app.route('/maggie')
def mags():
    """Return Maggie's own phrase."""
    return 'Maggie made this!!'

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
