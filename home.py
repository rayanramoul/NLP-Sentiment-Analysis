# -*- coding:utf-8 -*-
from flask import Flask, request, make_response, render_template
import os
from modals.evaluate import evaluate
app = Flask(__name__)
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

@app.route('/',methods=['GET','POST'])
def index():
    prediction=''
    if request.method == 'POST':
        prediction=str(evaluate(str(request.form['sentence'])))
        return render_template('index.html',prediction=prediction)        
    else:    
        return render_template('index.html',prediction='')



if __name__ == '__main__':
    app.run(debug=True)
