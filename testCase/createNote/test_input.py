import unittest
from copy import deepcopy
import time

from business.getIndexNote import get_index_list, get_calen_list, get_noteIndex_data
from common.aesfunc import aes_encry
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_common_note, create_calen_note, update_note
from common.checkOutput import CheckMethod
from common.readYaml import env_config


@class_case_log
class TestNoteinput(unittest.TestCase):
    header = env_config()['headers']

    # -----------------------cookie------------------------------------------
    def testCase01_create_note_invalidcookie_input(self):
        """上传便签cookie不存在"""
        expectBase = {
            "errorCode": -2010,
            "errorMsg": "",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['cookie'] = 'wps_sid=123'
        create_res = create_common_note(header=self.header)

        self.assertEqual(401, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase02_create_note_Bcookie_input(self):
        """上传便签cookie使用B用户"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "user change!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)
        self.header['cookie'] = 'wps_sid=V02SL9txH_cJPTIUPyg0DO65PZgklCI00a28340c0036f58bfd'
        create_res = create_common_note(header=self.header)
        self.assertEqual(412, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase03_create_note_removecookie_input(self):
        """上传便签cookie缺失"""
        expectBase = {
            "errorCode": -2009,
            "errorMsg": "",
        }
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header.pop('cookie')
        create_res = create_common_note(header=self.header)

        self.assertEqual(401, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase04_create_note_Nonecookie_input(self):
        """上传便签cookie值为None"""
        expectBase = {
            "errorCode": -2009,
            "errorMsg": "",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['cookie'] = None
        create_res = create_common_note(header=self.header)

        self.assertEqual(401, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase05_create_note_kcookie_input(self):
        """上传便签cookie值为空"""
        expectBase = {
            "errorCode": -2009,
            "errorMsg": "",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['cookie'] = ''
        create_res = create_common_note(header=self.header)

        self.assertEqual(401, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    # -----------------------xuserkey------------------------------------------
    def testCase06_create_note_removeuserkey_input(self):
        """上传便签x-user_key缺失"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "X-user-key header Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header.pop('X-user-key')
        create_res = create_common_note(header=self.header)

        self.assertEqual(412, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase07_create_note_Noneuserkey_input(self):
        """上传便签x-user_key为None"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "X-user-key header Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['X-user-key'] = None
        create_res = create_common_note(header=self.header)

        self.assertEqual(412, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase08_create_note_kuserkey_input(self):
        """上传便签x-user_key为空"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "X-user-key header Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['X-user-key'] = ''
        create_res = create_common_note(header=self.header)

        self.assertEqual(412, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase09_create_note_invaliduserkey_input(self):
        """上传便签x-user_key为无效"""
        expectBase = {
            "errorCode": -1011,
            "errorMsg": "user change!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        self.header['X-user-key'] = '123456'
        create_res = create_common_note(header=self.header)

        self.assertEqual(412, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    # -----------------------noteid------------------------------------------
    def testCase10_create_note_removenoteid_input(self):
        """上传便签noteid缺失"""
        expectBase = {
            "errorCode": -1000,
            "errorMsg": "NoteId Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {

        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase11_create_note_Nonenoteid_input(self):
        """上传便签noteid值为None"""
        expectBase = {
            "errorCode": -1000,
            "errorMsg": "NoteId Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': None
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase12_create_note_knoteid_input(self):
        """上传便签noteid值为空"""
        expectBase = {
            "errorCode": -1000,
            "errorMsg": "NoteId Requested!",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': ''
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase13_create_note_zhongwennoteid_input(self):
        """上传便签noteid值为中文"""
        expectBase = {
            "errorCode": -7,
            "errorMsg": "",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': '测试id'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase14_create_note_tesnoteid_input(self):
        """上传便签noteid值为特殊字符"""
        expectBase = {
            "errorCode": -7,
            "errorMsg": "",
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': '@#！'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase14_create_note_sqlnoteid_input(self):
        """上传便签noteid值为英文字符"""
        expectBase = {
            "responseTime": int, "infoVersion": int, "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': 'Hyyt'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase15_create_note_ENnoteid_input(self):
        """上传便签noteid值为'1 or 1=1'"""
        expectBase = {
            "responseTime": int, "infoVersion": int, "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': '1 or 1=1'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    # -----------------------remindtype------------------------------------------
    def testCase16_create_note_removeremindType_input(self):
        """上传便签remindType缺失"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase16_create_note_NoneremindType_input(self):
        """上传便签remindType值为None"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': None
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase17_create_note_kremindType_input(self):
        """上传便签remindType值为空"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': ''
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase18_create_note_0remindType_input(self):
        """上传便签remindType值为0"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': 0
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase18_create_note_1remindType_input(self):
        """上传便签remindType值为1"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': 1
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase19_create_note_2remindType_input(self):
        """上传便签remindType值为1"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': 2
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase19_create_note_xremindType_input(self):
        """上传便签remindType值为1.5"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': 1.5
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase20_create_note_zremindType_input(self):
        """上传便签remindType值为字符数值"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': "1"
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase21_create_note_chlremindType_input(self):
        """上传便签remindType值为随意数字超长"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindType': 1222322222222
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    # -----------------------remindtime------------------------------------------
    def testCase22_create_note_removeremindtime_input(self):
        """上传便签remindtime缺失"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase23_create_note_Noneremindtime_input(self):
        """上传便签remindtime值为None"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindtime': None
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase24_create_note_kremindtime_input(self):
        """上传便签remindtime值为空"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindtime': ''
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase25_create_note_0remindtime_input(self):
        """上传便签remindtime值为负数"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)
        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindtime': -11
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(500, create_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res.json())

    def testCase26_create_note_changremindtime_input(self):
        """上传便签remindtimetime值为长"""
        expectBase = {

            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindtime': 1122222222222634
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase27_create_note_2remindtime_input(self):
        """上传便签remindtime值为0"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'remindtime': 0
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    # -----------------------groupid------------------------------------------
    def testCase28_create_note_removegroupid_input(self):
        """上传便签groupid缺失"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase29_create_note_Nonegroupid_input(self):
        """上传便签groupid值为None"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': None
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase30_create_note_kgroupid_input(self):
        """上传便签groupid值为空"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': ''
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase31_create_note_zhongwengroupid_input(self):
        """上传便签groupid值为中文"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': '测试'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase32_create_note_tesgroupid_input(self):
        """上传便签groupid值为特殊字符"""
        expectBase = {
            "responseTime": int,
            "infoVersion": 1,
            "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': '!@###@'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase33_create_note_ENgroupid_input(self):
        """上传便签groupid值为英文字符"""
        expectBase = {
            "responseTime": int, "infoVersion": int, "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': 'Htyol'
        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    def testCase34_create_note_sqlgroupid_input(self):
        """上传便签groupid值为'1 or 1=1'"""
        expectBase = {
            "responseTime": int, "infoVersion": int, "infoUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
            'groupId': '1 or 1=1'

        }
        create_res = create_common_note(info_body=in_body)

        self.assertEqual(200, create_res[0].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, create_res[0].json())

    # ----------------------title------------------------------------------

    def testCase35_create_note_Nonetitle_input(self):
        """上传便签title值为None"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": None,
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase36_create_note_kongtitle_input(self):
        """上传便签title值为空"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": '',
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase37_create_note_removetitle_input(self):
        """上传便签title缺失"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    # ---------------------summary------------------------------------------
    def testCase38_create_note_Nonesummary_input(self):
        """上传便签summary值为None"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": None,
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase39_create_note_kongsummary_input(self):
        """上传便签summary值为空"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": '',
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase40_create_note_removesummary_input(self):
        """上传便签summary缺失"""
        expectBase = {
            "errorCode": -7, "errorMsg": "参数不合法！"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(500, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    # ---------------------body-----------------------------------------
    def testCase41_create_note_Nonebody_input(self):
        """上传便签body值为None"""
        expectBase = {
            "errorCode": -1012, "errorMsg": "Note body Requested!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": None,
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase42_create_note_kongbody_input(self):
        """上传便签body值为空"""
        expectBase = {
            "errorCode": -1012, "errorMsg": "Note body Requested!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": '',
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase43_create_note_removebody_input(self):
        """上传便签body缺失"""
        expectBase = {
            "errorCode": -1012, "errorMsg": "Note body Requested!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "localContentVersion": 1,
            "BodyType": 0
        }
        create_res = create_common_note(content_body=content_body, info_body=in_body)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    # ---------------------localContentVersion----------------------------------------
    def testCase44_create_note_NonelocalContentVersion_input(self):
        """上传便签localContentVersion值为None"""
        expectBase = {
            "errorCode": -1003, "errorMsg": "content version not equal!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": None,
            "BodyType": 0
        }
        create_common_note(content_body=content_body, info_body=in_body)
        create_res = update_note(in_body['noteId'], 'ceshi', 'ceshi', 'ceshi', localContentVersion=None)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase45_create_note_konglocalContentVersion_input(self):
        """上传便签localContentVersion值为空"""
        expectBase = {
            "errorCode": -1003, "errorMsg": "content version not equal!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": '',
            "BodyType": 0
        }
        create_common_note(content_body=content_body, info_body=in_body)
        create_res = update_note(in_body['noteId'], 'ceshi', 'ceshi', 'ceshi', localContentVersion=None)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase46_create_note_removelocalContentVersion_input(self):
        """上传便签localContentVersion缺失"""
        expectBase = {
            "errorCode": -1003, "errorMsg": "content version not equal!"
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)
        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": '',
            "BodyType": 0
        }
        create_common_note(content_body=content_body, info_body=in_body)
        create_res = update_note(in_body['noteId'], 'ceshi', 'ceshi', 'ceshi', localContentVersion=None, flag=1)

        self.assertEqual(412, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())

    def testCase47_create_note_xiaoshulocalContentVersion_input(self):
        """上传便签localContentVersion为小数"""
        expectBase = {
            "responseTime": int, "contentVersion": 2, "contentUpdateTime": int
        }

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)
        in_body = {
            'noteId': str(time.time() * 1000)[:-5],
        }
        content_body = {
            "noteId": in_body['noteId'],
            "title": aes_encry('ceshi'),
            "summary": aes_encry('ceshi'),
            "body": aes_encry('ceshi'),
            "localContentVersion": '',
            "BodyType": 0
        }
        create_common_note(content_body=content_body, info_body=in_body)
        create_res = update_note(in_body['noteId'], 'ceshi', 'ceshi', 'ceshi', localContentVersion=1.5)

        self.assertEqual(200, create_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, create_res[1].json())
