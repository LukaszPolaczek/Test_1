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
    wielodzietnosc = db.Column(db.Integer)
    wielmiasta = db.Column(db.Integer)
    stukoncz = db.Column(db.Integer)
    stzamiesz = db.Column(db.Integer)
    strodzice = db.Column(db.Integer)
    stgdzie = db.Column(db.String)
    ilepok = db.Column(db.String)
    ilewsplok = db.Column(db.String)
    ilezmian = db.Column(db.Integer)
    powzmian = db.Column(db.String)
    order = db.Column(db.String)
    znanewczesniej = db.Column(db.String)
    koedukacyjne = db.Column(db.String)
    gdzieszukane = db.Column(db.String)
    gdzieszukanetxt = db.Column(db.String)
    mpk = db.Column(db.Integer)
    czasprzejazdu = db.Column(db.Integer)
    rynekok = db.Column(db.Integer)
    wnioski = db.Column(db.String)


    def __init__(self, wiek, plec, wielodzietnosc, wielmiasta, stukoncz, stzamiesz, strodzice, stgdzie, ilepok, ilewsplok, ilezmian, powzmian, order, znanewczesniej, koedukacyjne, gdzieszukane, gdzieszukanetxt, mpk, czasprzejazdu, rynekok, wnioski):

        self.wiek = wiek
        self.plec = plec
        self.wielodzietnosc = wielodzietnosc
        self.wielmiasta = wielmiasta
        self.stukoncz = stukoncz
        self.stzamiesz = stzamiesz
        self.strodzice = strodzice
        self.stgdzie = stgdzie
        self.ilepok = ilepok
        self.ilewsplok = ilewsplok
        self.ilezmian = ilezmian
        self.powzmian = powzmian
        self.order = order
        self.znanewczesniej = znanewczesniej
        self.koedukacyjne = koedukacyjne
        self.gdzieszukane = gdzieszukane
        self.gdzieszukanetxt = gdzieszukanetxt
        self.mpk = mpk
        self.czasprzejazdu = czasprzejazdu
        self.rynekok = rynekok
        self.wnioski = wnioski

db.create_all()


@app.route("/")
def index():
    return render_template('base.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_database():
    data = db.session.query(Formdata).all()
    return render_template('raw.html', formdata = data)


@app.route("/save", methods=['POST'])
def add_todatabase():

    wiek = request.form['wiek']
    plec = request.form['plec']
    wielodzietnosc = request.form['wielodzietnosc']
    wielmiasta = request.form['wielmiasta']
    stukoncz = request.form['stukoncz']

    stzamiesz = request.form['stzamiesz']
    strodzice = request.form['strodzice']
    stgdzie = " studia gdzie" # request.form['stgdzie']
    ilepok = "ilo pokojowe" #request.form['ilepok']
    ilewsplok = "ile wspollokatorow" # request.form['ilewsplok']

    ilezmian = request.form['ilezmian']
    powzmian = request.form['powzmian']
    order = "kolejnosc czynnikow" #request.form['order']
    znanewczesniej = "czy znane wczesniej"# request.form['znanewczesniej']
    koedukacyjne = "koedukacyjne?"# request.form['koedukacyjne']

    gdzieszukane = "gdzie szukane" # request.form['gdzieszukane']
    gdzieszukanetxt = "gdzie szukane pole tekstowe" # request.form['gdzieszukanetxt']
    mpk = request.form['mpk']

    czasprzejazdu = request.form['czasprzejazdu']
    rynekok = request.form['rynekok']

    wnioski = request.form['wnioski']

    
    fd = Formdata(wiek, plec, wielodzietnosc, wielmiasta, stukoncz, stzamiesz, strodzice, stgdzie, ilepok, ilewsplok, ilezmian, powzmian, order, znanewczesniej, koedukacyjne, gdzieszukane, gdzieszukanetxt, mpk, czasprzejazdu, rynekok, wnioski)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)