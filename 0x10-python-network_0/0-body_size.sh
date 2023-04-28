#!/usr/bin/bash

# Get response size from url
curl -s "$1" | wc -c
