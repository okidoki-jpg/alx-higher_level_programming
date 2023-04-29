#!/usr/bin/env bash
# Send POST request to given URL & display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
