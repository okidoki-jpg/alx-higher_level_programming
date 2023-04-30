#!/usr/bin/python3
""" Display body response from a POST request to a given URL
with a given email using requests.

Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    r = requests.post(url, data=val)
    print(r.text)
