#!/usr/bin/env bash
# Display acceptable HTTP requests from given url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
