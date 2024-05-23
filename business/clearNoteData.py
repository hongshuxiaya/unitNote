from common.apiRe import post, get
from common.readYaml import env_config, data_config

host = env_config()['host']
userid = env_config()['userid']
headers = env_config()['headers']


def clear_note(noteId):
    del_url = host + data_config()['del_note']['path']
    body = {
        'noteId': noteId
    }
    del_res = post(url=del_url, headers=headers, body=body)
    return del_res


def clear_recyc_note(noteIds):
    comdel_url = host + data_config()['comdel_note']['path']
    note_list = []
    if isinstance(noteIds, str):
        note_list.append(noteIds)
    if isinstance(noteIds, list):
        note_list = noteIds
    if note_list != []:
        body = {
            'noteIds': note_list
        }

        del_res = post(url=comdel_url, headers=headers, body=body)
        return del_res
