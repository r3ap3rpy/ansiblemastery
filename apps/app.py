from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
        return "Welcome to Docker and Python."

@app.route("/hello")
def hello():
        return "Im just another context route."


if __name__ == '__main__':
        app.run(host="0.0.0.0", port = 9999, debug = True)