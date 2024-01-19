import os
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    usuario = os.environ["USER"]
    return usuario + " - Hello World!"

if __name__ == "__main__":
    application.run()
