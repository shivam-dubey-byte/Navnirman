#from app import app
from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']='afasdfasdfadfasdfad#'

@app.route("/")
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run()
