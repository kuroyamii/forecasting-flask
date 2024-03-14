from flask import Flask, request
import pkg.response.base as response
import flask_expects_json as validator
from internal.model.forecast import ForecastRequestBody
import pickle
import numpy as np
import pandas as pd



model = pickle.load(open('./model.pkl','rb')) 
feature_names = ['Order Month', 'Order Year', 'Product ID']

@validator.expects_json(ForecastRequestBody)
def forecast():
    print("INFO Forecasting Request")
    req = request.json
    month = req['month']
    year = req['year']
    product_id = req['product_id']

    # data = np.array([[month, year, product_id]])
    data = pd.DataFrame({"Order Month":[month],"Order Year":[year],"Product ID":[product_id]})
    print("INFO Predicting Result")
    model_res = model.predict(data)
    print("INFO Forecasting Result ->", model_res[0])
    res = {
        "month":month,
        "year":year,
        "product_id":product_id,
        "result":model_res[0]
    }
    print("INFO Returning Results")
    return response.success_response(res)

