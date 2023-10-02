#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys


def fetch_github_commits(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Error: Failed to fetch commits')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    fetch_github_commits(owner, repository)
