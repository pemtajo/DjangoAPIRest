#!/bin/bash

curl -X POST http://127.0.0.1:8000/sizes/ -H 'content-type: application/json' -d '{"description": "Large", "price": "40.00", "prepationTime": "25"}'
curl -X POST http://127.0.0.1:8000/sizes/ -H 'content-type: application/json' -d '{"description": "Medium", "price": "30.00", "prepationTime": "20"}'
curl -X POST http://127.0.0.1:8000/sizes/ -H 'content-type: application/json' -d '{"description": "Small", "price": "20.00", "prepationTime": "15"}'

curl -X POST http://127.0.0.1:8000/flavors/ -H 'content-type: application/json' -d '{"description": "calabresa", "addPrepationTime": "00"}'
curl -X POST http://127.0.0.1:8000/flavors/ -H 'content-type: application/json' -d '{"description": "marguerita", "addPrepationTime": "00"}'
curl -X POST http://127.0.0.1:8000/flavors/ -H 'content-type: application/json' -d '{"description": "portuguesa", "addPrepationTime": "05"}'

curl -X POST http://127.0.0.1:8000/adicionals/ -H 'content-type: application/json' -d '{"description": "Extra bacon", "addPrice": "03.00", "addPrepationTime": "00"}'
curl -X POST http://127.0.0.1:8000/adicionals/ -H 'content-type: application/json' -d '{"description": "Without onion", "addPrice": "00.00", "addPrepationTime": "00"}'
curl -X POST http://127.0.0.1:8000/adicionals/ -H 'content-type: application/json' -d '{"description": "Stuffed edge", "addPrice": "05.00", "addPrepationTime": "05"}'
