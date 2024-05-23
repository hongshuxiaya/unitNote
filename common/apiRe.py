import requests
from common.logCreate import info, error

from common.readYaml import env_config


def get(url, headers=None):
    if headers is None:
        headers = {
            "Cookie": env_config()['sid']
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    try:
        res = requests.get(url=url, headers=headers, timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return 'requests timeout!'
    info(f'【requests】code:{res.status_code}')
    info(f'【requests】body:{res.text}')
    return res


def post(url,body, headers=None):
    if headers is None:
        headers = {
            "Cookie": env_config()['sid']
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    info(f'【requests】body:{body}')
    try:
        res = requests.post(url=url, headers=headers,json=body,timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return 'requests timeout!'
    info(f'【requests】code:{res.status_code}')
    info(f'【requests】body:{res.text}')
    return res