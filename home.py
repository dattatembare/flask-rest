"""
Two routes for same API
Same result with
http://127.0.0.1:5000
And
http://127.0.0.1:5000/home
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Home Page<h1>"


if __name__ == '__main__':
    app.run()
