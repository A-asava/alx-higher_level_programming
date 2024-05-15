#!/bin/bash
# script that takes in a URL as an argument, sends a GET
curl -s -H "X-School-User-Id: 98" "$1"
