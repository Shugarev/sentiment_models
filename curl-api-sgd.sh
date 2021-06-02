#!/bin/sh

curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"config": {"profile": "sgd_classifier_multiclass", "vectorized_model": "tf_idf"},
"data": {
"text": "Celcuity Q EPS Misses Estimate"
}
}' \
 'http://0.0.0.0:8000/api/v4/check_text_order/'


