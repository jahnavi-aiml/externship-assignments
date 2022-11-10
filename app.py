# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:04:34 2021

@author: JahnaviP
"""
from flask import Flask,render_template,request#iimporting the flask library
import pickle
import joblib
model=pickle.load(open("profit.pkl",'rb'))
ct=joblib.load("column")
app=Flask(__name__) #creating an instance saying that u r creating flask application usong app name
@app.route('/') #app is routed with (bounded) with url '/'-localhost:5000
def helloworld():
    return render_template("index.html")
@app.route('/user/<name>') #app is routed with (bounded) with url '/'-localhost:5000
def user(name):
    return "welcome to smartbridge user"+' '+str(name)
@app.route('/guest') #app is routed with (bounded) with url '/'-localhost:5000
def guest():
    return "welcome to smartbridge user guest"
@app.route('/display',methods=['POST']) #app is routed with (bounded) with url '/'-localhost:5000
def display():
    ms=request.form['ms']
    ad=request.form['as']
    rs=request.form['rs']
    state=request.form['s']
    data=[[ms,ad,rs,state]]
    pred=model.predict(ct.transform(data))
    
    ls=["healthy","parkinson"]
        result = ls[preds[0]]
    return "result"
if __name__ =='__main__':   #main function
    app.run(debug=True)   # your app runs in local host
#binding urls==every wen appli has separate url binded to the main url

    