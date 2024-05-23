import time
from copy import deepcopy
from common.aesfunc import aes_decry
from common.apiRe import post, get
from common.readYaml import env_config, data_config

host = env_config()['host']
userid = env_config()['userid']
header = env_config()['headers']

get_calen_url = host + data_config()['getcalen_note']['path']


def get_index_note(startindex=None, rows=None,headers=None):
    if startindex is None:
        startindex = str(0)
    if rows is None:
        rows = str(99)
    if headers is None:
        headers=header
    get_url = host + data_config()['getindex_note']['path'].replace('{userid}', userid)
    get_url = get_url.replace('{startindex}', startindex).replace('{rows}', rows)
    get_res = get(get_url, headers=headers)
    if get_res.status_code==200:
        re_res = deepcopy(get_res.json())
        note_datas = get_res.json()['webNotes']
        for i in range(len(note_datas)):
            if note_datas[i]['title'] is None or 'test' in note_datas[i]['title']:
                continue
            if note_datas[i]['summary'] is None or 'test' in note_datas[i]['summary'] :
                continue
            re_res['webNotes'][i]['title'] = aes_decry(note_datas[i]['title'])
            re_res['webNotes'][i]['summary'] = aes_decry(note_datas[i]['summary'])

        return re_res,get_res
    return get_res


def get_calen_note(startTime=None, endTime=None, startIndex=None, rows=None,headers=None):
    if startTime is None:
        startTime = 1684663698
    if endTime is None:
        endTime = str(time.time() * 1000)[:-5]
    if startIndex is None:
        startIndex = str(0)
    if rows is None:
        rows = str(99)
    data = {
        "remindStartTime": startTime,
        "remindEndTime": endTime,
        "startIndex": startIndex,
        "rows": rows
    }
    if headers is None:
        headers=header
    get_res = post(get_calen_url, headers=headers, body=data)
    if get_res.status_code==200:
        re_res = deepcopy(get_res.json())
        note_datas = get_res.json()['webNotes']
        for i in range(len(note_datas)):
            if 'test' in note_datas[i]['title']:
                continue
            if 'test' in note_datas[i]['summary']:
                continue
            re_res['webNotes'][i]['title'] = aes_decry(note_datas[i]['title'])
            re_res['webNotes'][i]['summary'] = aes_decry(note_datas[i]['summary'])
        return re_res,get_res
    return get_res


def get_index_list():
    get_index_data = get_index_note()[0]
    note_list = []
    for note_cell in get_index_data['webNotes']:
        note_list.append(note_cell['noteId'])
    return note_list


def get_calen_list():
    get_calen_data = get_calen_note()[0]
    note_list = []
    for note_cell in get_calen_data['webNotes']:
        note_list.append(note_cell['noteId'])
    return note_list


def get_noteIndex_data(noteId):
    get_index_data = get_index_note()[0]
    for i in range(len(get_index_data['webNotes'])):
        if noteId == get_index_data['webNotes'][i]['noteId']:
            return get_index_data['webNotes'][i]
    return None


def get_noteCalen_data(noteId):
    get_index_data = get_calen_note()[0]
    for i in range(len(get_index_data['webNotes'])):
        if noteId == get_index_data['webNotes'][i]['noteId']:
            return get_index_data['webNotes'][i]
    return None
