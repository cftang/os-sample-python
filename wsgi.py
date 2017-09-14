from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! python 3.5"

if __name__ == "__main__":
    application.run()
