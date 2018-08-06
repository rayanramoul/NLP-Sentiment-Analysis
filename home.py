# -*- coding:utf-8 -*-
from flask import Flask, request, make_response, render_template
import os
from modals.evaluate import evaluate
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)


class comment(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	sentence= db.Column(db.String(80),unique=False,nullable=False)
	sentiment=db.Column(db.String(30),unique=False,nullable=False)
	def __repr__(self):
		return '<comment \'%r\'>' % self.comment






@app.route('/',methods=['GET','POST'])
def index():
    prediction=''
    if request.method == 'POST':
        prediction=str(evaluate(str(request.form['sentence'])))
        return render_template('index.html',prediction=prediction,sentence=str(request.form['sentence']))        

    else:    
        return render_template('index.html',prediction='')



@app.route('/comment/',methods=['GET','POST'])
def Comment():
    if request.method == 'POST':
    	sentence=request.form['sentence']
    	sentiment=request.form['sentiment']
    	com=comment(sentence=sentence,sentiment=sentiment)
    	db.session.add(com)
    	db.session.commit()
    	return render_template('index.html',prediction='')
    if request.args.get('sentence', None):
    	sentence = str(request.args['sentence'])
    	return render_template('comment.html',sentence=sentence)
    	
    else:    
        return render_template('comment.html',prediction='')



if __name__ == '__main__':
    app.run(debug=True)
