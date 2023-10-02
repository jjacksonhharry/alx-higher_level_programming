#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""


def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        json_response = response.json()

        if json_response:
            print("[{}] {}".format(
                json_response.get('id'),
                json_response.get('name')))
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user(letter)
