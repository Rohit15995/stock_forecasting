from flask import render_template, url_for, flash, redirect, request
from stockforecasting import app
from stockforecasting.forms import PredictionForm

@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
@app.route("/predict", methods=['GET','POST'])

def predict():
    form = PredictionForm()
    return render_template('predict.html', form=form)