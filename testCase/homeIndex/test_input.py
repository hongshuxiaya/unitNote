import unittest
from copy import deepcopy
from business.getIndexNote import get_index_list, get_index_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_recyc_note, clear_note
from business.createNoteData import create_common_note
from common.checkOutput import CheckMethod
from common.readYaml import env_config


@class_case_log
class TestGetMajor(unittest.TestCase):
    def testCase01_get_note_invalidcookie_input(self):
        """查看便签wps_si不存在"""
        expectBase = {
            "errorCode":-2009,"errorMsg":""
        }

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_common_note()
        header = env_config()['headers']
        header.pop('cookie')
        calen_res=get_index_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase02_get_note_Bcookie_input(self):
        """查看日历便签wps_siB用户"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "user change!",
        }
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_common_note()
        header = env_config()['headers']
        header['cookie'] = 'wps_sid=V02SL9txH_cJPTIUPyg0DO65PZgklCI00a28340c0036f58bfd'
        calen_res = get_index_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
