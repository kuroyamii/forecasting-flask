ForecastRequestBody = {
    "type":"object",
    "properties":{
        "month":{
            "type":"integer"
        },
        "year":{
            "type":"integer"
        },
        "sub_category":{
            "type":"string"
        }
    },
    "required":["month","year","sub_category"]
}