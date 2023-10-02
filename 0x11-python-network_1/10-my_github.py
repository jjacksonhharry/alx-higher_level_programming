#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


def get_github_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        return user_info.get('id')
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <password>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    github_id = get_github_id(username, password)
    print(github_id)
