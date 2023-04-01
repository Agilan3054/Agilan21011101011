from flask import Flask,render_template, request, url_for
from flask_mysqldb import MySQL
import mysql.connector

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
       


def pred(li):
    data=pd.read_csv("C:\\B Drive\\downloads\\diabetes.csv")
    df=pd.DataFrame(data)
    x=df.iloc[:,:-1]
    y=df.iloc[:,8]
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)
    s1=SVC(kernel='linear',random_state=0)
    s1.fit(x_train,y_train)
    y_pred=s1.predict(x_test)
    return (y_pred)

 
app = Flask(_name_)
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4243",
        database="flask"
        )
cursor = mydb.cursor()

@app.route('/')
def form():
    return render_template('home.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('log.html')
     
    if request.method == 'POST':

        username = request.form.get("username")
        password = request.form.get("password")
        l=(username,password)
        flag=0
        cursor.execute("select * from login ")
        output = cursor.fetchall()
        for i in output:
            if(l==i):
                print(i)
                flag=1
        if(flag==0):
             return ("login invalid")
        else:
            return render_template("quiz.html")
        
        
    return render_template('log.html')
 
@app.route('/quiz', methods = ['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html')
     
    if request.method == 'POST':
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = int (request.form.get("Glucose"))
        BloodPressure = int (request.form.get("BloodPressure"))
        SkinThickness =int (request.form.get("SkinThickness"))
        Insulin = int (request.form.get("Insulin"))
        BMI = float ( request.form.get("BMI"))
        DiabetesPedigreeFunction = int (request.form.get("extraversion"))
        Age = int (request.form.get("Age"))
        li=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction, Age]]
        result=pred(li)
        return result

    return render_template("quiz.html")

        
app.run(host='localhost', port=5000)
