from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:pgadmin@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://txgwglmdukzzmv:27fd9a7c10f68301cf5e8706139216ee21037e7cebc08a4bf2cff0c573f8d0c1@ec2-23-21-4-7.compute-1.amazonaws.com:5432/db6gef1hcl9cst'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(5000))

# This trigger whenever anyone visits
# / is default or home page
# route is a decorator

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process',methods = ['POST'] )
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
