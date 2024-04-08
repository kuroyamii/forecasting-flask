from flask import Flask, request
import pkg.response.base as response
import flask_expects_json as validator
from internal.model.forecast import ForecastRequestBody
import pickle
import numpy as np
import pandas as pd
import os
import mysql.connector as connector


model = pickle.load(open('./model.pkl','rb'))
# models = {}
# for item in os.listdir("./ml_model"):
#     model = pickle.load(open("./ml_model/{}".format(item),"rb"))
#     name = item.split("_")[1]
#     models[name] = model


feature_names = ['Order Month', 'Order Year']
# Database connection
dbconn = connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="superstore_dataset"
)
cursor = dbconn.cursor()
qr = "SELECT * from sub_categories"
cursor.execute(qr)
sc = cursor.fetchall()
sub_categories = []
for item in sc:
    sub_categories.append(item[1])
dbconn.close()

@validator.expects_json(ForecastRequestBody)
def forecast():
    print("INFO Forecasting Request")
    req = request.json
    month = req['month']
    year = req['year']
    sub_category = req['sub_category']
    sc_data = {}
    # Validates sub_categories
    if sub_category not in sub_categories:
        return response.error_response("invalid sub category",400,"BAD REQUEST")

    if month < 1 or month > 12:
        return response.error_response("invalid month",400,"BAD REQUEST")


    for item in sub_categories:
        sc_data[item] = [0.0]
        if sub_category == item:
            sc_data[item] = [1.0]
    sc_data.update({"Order Month":[month],"Order Year":[year]})
    data = pd.DataFrame(sc_data)
    


    # Forecast using model
    print("INFO Predicting Result")
    model_res = model.predict(data)
    print("INFO Forecasting Result ->", model_res[0])
    res = {
        "month":month,
        "year":year,
        "sub_category":sub_category,
        "result":model_res[0]
    }
    print("INFO Returning Results")
    return response.success_response(res)

