from datetime import datetime, timedelta
import random
import time
from common.aesfunc import aes_encry
from common.readYaml import env_config, data_config
from common.apiRe import post

host = env_config()['host']
userid = env_config()['userid']
headers = env_config()['headers']
create_info_url = host + data_config()['create_info']['path']
create_content_url = host + data_config()['create_content']['path']


def create_common_note(header=None, content_body=None,  info_body=None):
    title = 'title测试数据'
    summary = 'summary测试数据'
    body = 'body测试数据'
    if header is None:
        header = headers
    if info_body is None:
        noteId = str(time.time() * 1000)[:-5]
        star = random.randint(0, 1)
        info_body = {
            "noteId": noteId,
            "star": star
        }
    info_res = post(url=create_info_url, headers=header, body=info_body)
    if info_res.status_code == 200:
        if content_body is None:
            content_body = {
                "noteId": info_body['noteId'],
                "title": aes_encry(title),
                "summary": aes_encry(summary),
                "body": aes_encry(body),
                "localContentVersion": 1,
                "BodyType": 0
            }
        content_res = post(url=create_content_url, headers=header, body=content_body)
        info_body.update(content_body)
        info_body['title'] = title
        info_body['summary'] = summary
        info_body['body'] = body
        return info_res, content_res, info_body
    return info_res


def create_calen_note(header=None, content_body=None,info_body=None):
    title = 'title测试数据'
    summary = 'summary测试数据'
    body = 'body测试数据'
    if header is None:
        header = headers

    two_days_later = datetime.now() + timedelta(days=2)
    remindTime = time.mktime(two_days_later.timetuple())
    if header is None:
        header = headers
    if info_body is None:
        noteId = str(time.time() * 1000)[:-5]
        star = random.randint(0, 1)
        remindType = random.randint(0, 2)
        info_body = {
            "noteId": noteId,
            "star": star,
            "remindTime": remindTime,
            "remindType": remindType
        }
    info_res = post(url=create_info_url, headers=header, body=info_body)
    if info_res.status_code == 200:
        if content_body is None:
            content_body = {
                "noteId": info_body['noteId'],
                "title": aes_encry(title),
                "summary": aes_encry(summary),
                "body": aes_encry(body),
                "localContentVersion": 1,
                "BodyType": 0
            }
        content_res = post(url=create_content_url, headers=header, body=content_body)

        info_body.update(content_body)
        info_body['title'] = title
        info_body['summary'] = summary
        info_body['body'] = body
        return info_res, content_res, info_body
    return info_res


def update_note(noteId, title, summary, body, localContentVersion, remindTime=0, remindType=0,flag=0):
    info_body = {
        "noteId": noteId,
        "remindTime": remindTime,
        "remindType": remindType
    }
    if flag==1:
        content_body = {
            "noteId": noteId,
            "title": aes_encry(title),
            "summary": aes_encry(summary),
            "body": aes_encry(body),
            "BodyType": 0
        }
    else:
        content_body = {
            "noteId": noteId,
            "title": aes_encry(title),
            "summary": aes_encry(summary),
            "body": aes_encry(body),
            "localContentVersion": localContentVersion,
            "BodyType": 0
        }
    info_res = post(url=create_info_url, headers=headers, body=info_body)
    if info_res.status_code == 200:
        content_res = post(url=create_content_url, headers=headers, body=content_body)
        info_body.update(content_body)
        info_body['title'] = title
        info_body['summary'] = summary
        info_body['body'] = body
        return info_res, content_res, info_body
    return info_res
