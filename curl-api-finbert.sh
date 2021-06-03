#!/bin/sh

curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"config": {"profile": "pytorch_model.bin"},
"data": {
"text": "Trex Co Q1 EPS $0.42 Beats $0.38 Estimate, Sales $245.52M Beat $238.26M Estimate; Reaffirms FY21 Incremental EBITDA Margin Guidance 35-40%"
}
}' \
 'http://0.0.0.0:8000/api/v4/check_text_order/'


# Penske Automotive Q1 results beat estimates, with revenue growth of 15.3% - positive
# Celcuity Q EPS Misses Estimate - negative
# Penske Automotive Q1 results beat estimates, with revenue growth of 15.3%. Celcuity Q EPS Misses Estimate.
# Great Western Bancorp Q2 EPS  0.93𝐵𝑒𝑎𝑡𝑠 0.61 Estimate, Sales  120.06𝑀𝐵𝑒𝑎𝑡 117.44M Estimate -  positive/negative
# Verrica Pharmaceuticals Q1 EPS  (0.04)𝑈𝑝𝐹𝑟𝑜𝑚 (0.39) YoY - positive/negative
# Protagonist Therapeutics Q1 EPS $(0.54) Up From $(0.72) YoY, Sales $6.19M Up From $3.65M YoY - positive
# Benzinga Top Ratings Upgrades, Downgrades For May 5, 2021 - negative
# Diffusion Pharmaceuticals Q1 EPS $(0.06) Misses $(0.04) Estimate - negative
# Trex Co Q1 EPS $0.42 Beats $0.38 Estimate, Sales $245.52M Beat $238.26M Estimate; Reaffirms FY21 Incremental EBITDA Margin Guidance 35-40% - positive