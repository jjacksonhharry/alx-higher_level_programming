#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: {} <URL>".format(argv[0]))
        return

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print("Error:", e.reason)


if __name__ == "__main__":
    main()
