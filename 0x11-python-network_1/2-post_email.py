#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


def main():
    if len(argv) != 3:
        print("Usage: {} <URL> <email>".format(argv[0]))
        return

    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))


if __name__ == "__main__":
    main()
