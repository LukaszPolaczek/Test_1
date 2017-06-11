from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///baza1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata (db.Model):
    __tablename__='baza1'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    wiek = db.Column(db.Integer)
    plec = db.Column(db.Integer)
    czynsz = db.Column(db.Integer)
    gmiesz = db.Column(db.Integer)
    Wcena  = db.Column(db.Integer)
    Wstand = db.Column(db.Integer)
    Wloka  = db.Column(db.Integer)


    def __init__(self, wiek, plec, czynsz, gmiesz, Wcena, Wstand, Wloka):

        self.wiek = wiek
        self.plec = plec
        self.czynsz = czynsz
        self.gmiesz = gmiesz
        self.Wcena = Wcena
        self.Wstand = Wstand
        self.Wloka = Wloka

db.create_all()


@app.route("/")
def index():
    return render_template('form.html')


@app.route("/raw")
def show_database():
    data = db.session.query(Formdata).all()
    return render_template('raw.html', formdata = data)


@app.route("/result")
def show_result():

    # Przykład przesyłania danych z pomocą dictionary

    TempDictToResult = {}

    TempAvarage = 34
    TempTable = [11,23,5]
    TempDict = {'Namber1':34,'Table1':[56,41]}

    TempDictToResult['TempAvarageName']= TempAvarage
    TempDictToResult['TempTableName']  = TempTable
    TempDictToResult['TempDictName']   = TempDict

    return render_template('result.html',TempSent=TempDictToResult)

@app.route("/save", methods=['POST'])
def add_todatabase():

    wiek = request.form['wiek']
    plec = request.form['plec']
    czynsz = request.form['czynsz']
    gmiesz = request.form['gmiesz']
    Wcena = request.form['Wcena']
    Wstand = request.form['Wstand']
    Wloka = request.form['Wloka']

    
    fd = Formdata(wiek, plec, czynsz, gmiesz, Wcena, Wstand, Wloka)
    db.session.add(fd)
    db.session.commit()

    return redirect('/result')


if __name__ == '__main__':
    app.run(debug=True)