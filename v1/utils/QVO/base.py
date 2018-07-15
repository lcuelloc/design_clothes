import requests


def _test_url():
    return "https://playground.qvo.cl/"


def _prod_url():
    return "https://playground.qvo.cl/"


def _base_url(url, dev):
    if dev is True:
        return _test_url()+url
    elif dev is False:
        return _prod_url()+url
    else:
        return None


def _headers(token):
    if token is not None:
        return {'Authorization': 'bearer '+token}
    return None


def get_params(**kwargs):
    url = _base_url(kwargs.get('url'), kwargs.get('dev'))
    if url is not None:
        headers = _headers(kwargs.get('token'))
        params = kwargs.get('params')
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 404:
            return None
        content = response.json()
        return content
    return None


def post_json(**kwargs):
    url = _base_url(kwargs.get('url'), kwargs.get('dev'))
    if url is not None:
        headers = _headers(kwargs.get('token'))
        params = kwargs.get('params')
        json = kwargs.get('json')
        response = requests.post(
            url, headers=headers, params=params, json=json)
        content = response.json()
        return content
    return None
