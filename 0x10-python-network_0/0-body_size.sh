#!/usr/bin/env bash
# Get response size from url
curl -s "$1" | wc -c
