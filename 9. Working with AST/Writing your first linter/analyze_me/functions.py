import requests


def check_200(response):
    try:
        return True if response.status_code is 200 else False
    except:
        pass
    return False


def request_google():
    return requests.get('https://google.com')
