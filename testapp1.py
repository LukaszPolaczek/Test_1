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
    fd_list = db.session.query(Formdata).all()

    # Count statistics for chart 1:
    cost1 = 0
    cost2 = 0
    cost3 = 0
    standard1 = 0
    standard2 = 0
    standard3 = 0
    location1 = 0
    location2 = 0
    location3 = 0
    values_not_in_range = []
    counter = 0
    meanAge = 0
    meanRent = 0
    placeToLive = []

    for el_cost in fd_list:
        if int(el_cost.Wcena) == 1:
            cost1 += 1
        if int(el_cost.Wcena) == 2:
            cost2 += 1
        if int(el_cost.Wcena) == 3:
            cost3 += 1
        else:
            values_not_in_range.append(int(el_cost.Wcena))
            # we should throw some exception here

    for el_standard in fd_list:
        if int(el_standard.Wstand) == 1:
            standard1 += 1
        if int(el_standard.Wstand) == 2:
            standard2 += 1
        if int(el_standard.Wstand) == 3:
            standard3 += 1
        else:
            values_not_in_range.append(int(el_standard.Wstand))
            # we should throw some exception here

    for el_location in fd_list:
        if int(el_location.Wloka) == 1:
            location1 += 1
        if int(el_location.Wloka) == 2:
            location2 += 1
        if int(el_location.Wloka) == 3:
            location3 += 1
        else:
            values_not_in_range.append(int(el_location.Wloka))
            # we should throw some exception here

    for count in fd_list:
        counter = counter+1


    for list in fd_list:
        meanAge = meanAge + list.wiek
        meanRent = meanRent +list.czynsz


    meanAge = meanAge/counter
    meanRent = meanRent/counter



    for place in db.engine.execute("select gmiesz from baza1"):
        placeToLive.append(place.gmiesz)


    list=[]
    for x in range (1,6):
        list.append(placeToLive.count(x))

    # list = placeToLive.count(1)

    # Prepare data for google charts
    data_for_chart_1 = [['Cena', cost1, cost2, cost3], ['Standard', standard1, standard2, standard3], ['Lokalizacja', location1, location2, location3]]
    return render_template('result.html', data_for_chart_1=data_for_chart_1, counter = counter, meanAge = meanAge, meanRent = meanRent, placeToLive=placeToLive, list=list)

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