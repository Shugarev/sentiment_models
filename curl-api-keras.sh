#!/bin/sh

curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"config": {"profile": "keras_cnn_multiclass_model.hdf5", "tokenizer_model": "tokenizer_model"},
"data": {
"text": "Celcuity Q EPS Misses Estimate"
}
}' \
 'http://0.0.0.0:8000/api/v4/check_text_order/'


