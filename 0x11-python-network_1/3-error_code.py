#!/usr/bin/python3
""" Display body reaponse of request to a given URL and handle HTTP errors

Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
