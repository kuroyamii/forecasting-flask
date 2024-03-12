ForecastRequestBody = {
    "type":"object",
    "properties":{
        "month":{
            "type":"integer"
        },
        "year":{
            "type":"integer"
        },
        "product_id":{
            "type":"integer"
        }
    },
    "required":["month","year","product_id"]
}