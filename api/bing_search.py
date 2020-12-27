from flask import Flask
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
@app.route("/welcome")
def welcome():
    return "<h1>Welcome!!!<h1>"


@app.route("/bing/<q>")
def bing_search(q='Hello'):
    return redirect(f"https://www.bing.com/search?q={q}")


if __name__ == '__main__':
    app.run()
