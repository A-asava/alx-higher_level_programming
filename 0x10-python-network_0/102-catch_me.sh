#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server 
curl -s --data "user_id=98" -X PUT  0.0.0.0:5000/catch_me
