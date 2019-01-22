from flask import Flask
from flask import render_template
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/time')
def show_time():
    t = str(datetime.datetime.now())
    return 'time : %s ' % t

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

