import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        t = np.array(dict1["data"]).astype('float32')
        print(t[0]+t[1])
        t[0] += t[1]
        tt = t.astype(str).tolist()
        return json.dumps(tt)
    else:
        return '<h1>Only post!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> hello, %s</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)

