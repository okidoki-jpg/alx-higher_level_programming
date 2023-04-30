#!/usr/bin/python3
""" Send POST request to a URL with a given letter saved to var 'q'.

Usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    val = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=val)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print(f'[{res.get("id")}] {res.get("name")}')
    except ValueError:
        print("Not a valid JSON")
