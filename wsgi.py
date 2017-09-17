from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! python 3.5"

@application.route("/map1")
def hello():
    return "Hello World! map1"

@application.route("/map2")
def hello():
    return "Hello World! map2"

@application.route("/map3")
def hello():
    return "Hello World! map3"

if __name__ == "__main__":
    application.run()
