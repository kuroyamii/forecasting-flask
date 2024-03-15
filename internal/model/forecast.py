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
        },
        "discount":{
            "type":"number"
        }
    },
    "required":["month","year","sub_category","discount"]
}