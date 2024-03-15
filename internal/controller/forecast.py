from flask import Flask, request
import pkg.response.base as response
import flask_expects_json as validator
from internal.model.forecast import ForecastRequestBody
import pickle
import numpy as np
import pandas as pd
import os


# model = pickle.load(open('./model.pkl','rb'))
models = {}
for item in os.listdir("./ml_model"):
    model = pickle.load(open("./ml_model/{}".format(item),"rb"))
    name = item.split("_")[1]
    models[name] = model


feature_names = ['Order Month', 'Order Year', 'Discount']

@validator.expects_json(ForecastRequestBody)
def forecast():
    print("INFO Forecasting Request")
    req = request.json
    month = req['month']
    year = req['year']
    sub_category = req['sub_category']
    discount = req['discount']

    data = pd.DataFrame({"Discount":[discount],"Order Month":[month],"Order Year":[year]})



    # Forecast using model
    print("INFO Predicting Result")
    model_res = models[sub_category+".pkl"].predict(data)
    print("INFO Forecasting Result ->", model_res[0])
    res = {
        "month":month,
        "year":year,
        "sub_category":sub_category,
        "result":model_res[0]
    }
    print("INFO Returning Results")
    return response.success_response(res)

