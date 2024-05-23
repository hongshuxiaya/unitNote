import time
from copy import deepcopy
from common.aesfunc import aes_decry
from common.apiRe import post, get
from common.readYaml import env_config, data_config

host = env_config()['host']
userid = env_config()['userid']
headers = env_config()['headers']


def get_recyc_note(startindex=None, rows=None):
    if startindex is None:
        startindex = str(0)
    if rows is None:
        rows = str(99)
    get_url = host + data_config()['recyc_note']['path'].replace('{userid}', userid)
    get_url = get_url.replace('{startindex}', startindex).replace('{rows}', rows)
    get_res = get(get_url, headers=headers)
    re_res = deepcopy(get_res.json())
    note_datas = get_res.json()['webNotes']
    for i in range(len(note_datas)):
        if 'test' in note_datas[i]['title']:
            continue
        if 'test' in note_datas[i]['summary']:
            continue
        re_res['webNotes'][i]['title'] = aes_decry(note_datas[i]['title'])
        re_res['webNotes'][i]['summary'] = aes_decry(note_datas[i]['summary'])
    return re_res



get_recyc_note()