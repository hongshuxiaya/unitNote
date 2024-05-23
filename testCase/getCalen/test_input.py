import unittest
from business.getIndexNote import get_calen_list, get_calen_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_calen_note
from common.checkOutput import CheckMethod
from common.readYaml import env_config


@class_case_log
class TestGetCalenMajorinput(unittest.TestCase):

    def testCase01_get_note_invalidcookie_input(self):
        """查看日历便签wps_si不存在"""
        expectBase = {
            "errorCode":-2009,"errorMsg":""
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header.pop('cookie')
        calen_res=get_calen_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase02_get_note_Bcookie_input(self):
        """查看日历便签wps_siB用户"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "user change!",
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header['cookie']='wps_sid=V02SL9txH_cJPTIUPyg0DO65PZgklCI00a28340c0036f58bfd'
        calen_res = get_calen_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
