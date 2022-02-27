#import flask
from flask import Flask

#Create new flask instance
app = Flask(__name__)

#Create flask rout
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/Help')
def Help():
    return 'There is no help for you'