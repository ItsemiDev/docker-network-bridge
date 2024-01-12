import requests


def make_request():
    try:
        response = requests.get("http://server:8000")
        print(response.text)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


if __name__ == "__main__":
    make_request()
