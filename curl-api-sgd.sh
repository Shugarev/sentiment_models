#!/bin/sh

curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"config": {"profile": "sgd_classifier_multiclass", "vectorized_model": "tf_idf"},
"data": {
"text": "Penske Automotive Q1 results beat estimates, with revenue growth of 15.3%"
}
}' \
 'http://0.0.0.0:8000/api/v4/check_text_order/'


#Penske Automotive Q1 results beat estimates, with revenue growth of 15.3% - positive
#Celcuity Q EPS Misses Estimate - negative