from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd


model=pickle.load(open("/home/exterminator/train/Smart_internz_project/model_dc.pkl",'rb'))
app=Flask(__name__)

dict_val= {'PAYMENT':0, 'TRANSFER':1 ,'CASH OUT':2 ,'DEBIT':3 ,'CASH_IN':4}
@app.route("/")
def start():
    return render_template('index.html')

@app.route("/predict")
def predict():
    return render_template('predict.html')

@app.route("/Home")
def index():
    return render_template('index.html')

@app.route("/login",methods=['POST'])
def login():
    x=[[x for x in request.form.values()]]
    x=np.array(x)
    print(x)
    # pred=model.predict(x)
    x[0][1]=dict_val[x[0][1]]
    print(x)
    x=x.astype(float)
    output=model.predict(x)
    val=""
    if(output[0]==0):
        val="Not Fraud"
    else:
        val="Fraud"
    return render_template('submit.html',y=val)
    
if(__name__=="__main__"):
    app.run(debug=True)