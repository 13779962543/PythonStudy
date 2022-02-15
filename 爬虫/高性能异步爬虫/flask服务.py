from flask import Flask
import time

app=Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/lei')
def index_lei():
    time.sleep(2)
    return 'Hello lei'

@app.route('/bai')
def index_bai():
    time.sleep(2)
    return 'Hello bai'

if __name__=='__main__':
    app.run(threaded=True)