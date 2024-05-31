import time
import unittest
from copy import deepcopy

from business.getIndexNote import get_calen_list, get_calen_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_calen_note
from common.checkOutput import CheckMethod
from common.readYaml import env_config,data_config


@class_case_log
class TestGetCalenMajorinput(unittest.TestCase):
    body=data_config()['getcalen_note']['body']

    def testCase01_get_note_invalidcookie_input(self):
        """查看日历便签cookie不存在"""
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
        """查看日历便签cookieB用户"""
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

    def testCase03_get_note_removecookie_input(self):
        """查看日历便签cookie缺失"""
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
        calen_res = get_calen_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
    #--------------------X-user-key----------------------------
    def testCase04_get_note_invalidXuserkey_input(self):
        """查看日历便签X-user-key不存在"""
        expectBase = {
            "errorCode":-1011,"errorMsg":"user change!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header['X-user-key']='1234567890'
        calen_res = get_calen_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase05_get_note_Nonexuserkey_input(self):
        """查看日历便签X-user-key为None"""
        expectBase = {
            "errorCode":-1011,"errorMsg":"X-user-key header Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header['X-user-key'] = None
        calen_res = get_calen_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase06_get_note_removexuserkey_input(self):
        """查看日历便签X-user-key缺失"""
        expectBase = {
            "errorCode":-1011,"errorMsg":"X-user-key header Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header.pop('X-user-key')
        calen_res = get_calen_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase07_get_note_kongxuserkey_input(self):
        """查看日历便签X-user-key为空"""
        expectBase = {
            "errorCode": -1011, "errorMsg": "X-user-key header Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        header = env_config()['headers']
        header['X-user-key']=''
        calen_res = get_calen_note(headers=header)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    # --------------------remindStartTime----------------------------
    def testCase08_get_note_NoneremindStartTime_input(self):
        """查看日历便签remindStartTime为None"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body['remindStartTime']=None
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase09_get_note_removeremindStartTime_input(self):
        """查看日历便签remindStartTime缺失"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body.pop('remindStartTime')
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase10_get_note_kongremindStartTime_input(self):
        """查看日历便签remindStartTime为空"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body['remindStartTime'] = ''
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase11_get_note_zifuremindStartTime_input(self):
        """查看日历便签remindStartTime为字符串"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindStartTime'] = '1684663698'
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(412, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase12_get_note_xiaoshuremindStartTime_input(self):
        """查看日历便签remindStartTime为小数"""
        expectBase = {
            "errorCode":-7,"errorMsg":""
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindStartTime'] = '1.5'
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(500, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase13_get_note_dayuremindStartTime_input(self):
        """查看日历便签remindStartTime为大于日历设置start时间"""
        expectBase = {"responseTime":0,"webNotes":[]}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindStartTime'] = int(str(time.time() * 1000)[:-5])
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res[1].json())


    def testCase12_get_note_dayuuremindStartTime_input(self):
        """查看日历便签remindStartTime为大于日历设置end时间"""
        expectBase = {"errorCode":-7,"errorMsg":"remindTime Requested!"}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindStartTime'] = int(str(time.time() * 1000)[:-5])
        self.body['remindEndTime'] = int(str(time.time() * 1000)[:-8])
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(412, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    # --------------------remindendTime----------------------------
    def testCase13_get_note_NoneremindEndTime_input(self):
        """查看日历便签remindendTime为None"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body['remindEndTime']=None
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase14_get_note_removeremindEndTime_input(self):
        """查看日历便签remindEndTime缺失"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body.pop('remindEndTime')
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase15_get_note_kongremindEndTime_input(self):
        """查看日历便签remindEndTime为空"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_calen_note()
        self.body['remindEndTime'] = ''
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase16_get_note_zifuremindEndTime_input(self):
        """查看日历便签remindStartTime为字符串"""
        expectBase = {
            "errorCode":-7,"errorMsg":"remindTime Requested!"
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindStartTime'] = '168466369811'
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(412, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase17_get_note_xiaoshuremindEndTime_input(self):
        """查看日历便签remindStartTime为小数"""
        expectBase = {
            "errorCode":-7,"errorMsg":""
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['remindEndTime'] = '1.5'
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(500, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    # --------------------startIndex----------------------------
    def testCase18_get_note_NonestartIndex_input(self):
        """查看日历便签startIndex为None"""
        expectBase = {
        "responseTime": int,
        "webNotes": [
            {
                "noteId": str,
                "createTime": int,
                "star": 0,
                "remindTime": int,
                "remindType": int,
                "infoVersion": 1,
                "infoUpdateTime": int,
                "groupId": None,
                "title": str,
                "summary": str,
                "thumbnail": None,
                "contentVersion": 1,
                "contentUpdateTime": int
            }
        ]
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['startIndex'] = None
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        expect = deepcopy(expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, calen_res[0])

    def testCase19_get_note_kongstartIndex_input(self):
        """查看日历便签startIndex为空"""
        expectBase = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": 0,
                    "remindTime": int,
                    "remindType": int,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": str,
                    "summary": str,
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }
            ]
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res = create_calen_note()
        self.body['startIndex'] = ''
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        expect = deepcopy(expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, calen_res[0])

    def testCase20_get_note_removestartIndex_input(self):
        """查看日历便签startIndex缺失"""
        expectBase = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": 0,
                    "remindTime": int,
                    "remindType": int,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": str,
                    "summary": str,
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }
            ]
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res = create_calen_note()
        self.body.pop('startIndex')
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        expect = deepcopy(expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, calen_res[0])

    def testCase21_get_note_dayuremindstartIndex_input(self):
        """查看日历便签startIndex为大于便签数"""
        expectBase = {"responseTime":0,"webNotes":[]}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['startIndex'] = '2'
        calen_res = get_calen_note(data=self.body)
        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res[1].json())

    def testCase22_get_note_zifustartIndex_input(self):
        """查看日历便签startIndex为特殊字符"""
        expectBase = {
            "errorCode":-7,"errorMsg":""
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res = create_calen_note()
        self.body['startIndex']='@#@@@@'
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(500, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())

    # --------------------rows----------------------------
    def testCase23_get_note_Nonerows_input(self):
        """查看日历便签rows为None"""
        expectBase = {
        "responseTime": int,
        "webNotes": [
            {
                "noteId": str,
                "createTime": int,
                "star": 0,
                "remindTime": int,
                "remindType": int,
                "infoVersion": 1,
                "infoUpdateTime": int,
                "groupId": None,
                "title": str,
                "summary": str,
                "thumbnail": None,
                "contentVersion": 1,
                "contentUpdateTime": int
            }
        ]
    }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res=create_calen_note()
        self.body['rows'] = None
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        expect = deepcopy(expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, calen_res[0])

    def testCase24_get_note_zifurows_input(self):
        """查看日历便签rows为特殊字符"""
        expectBase = {
            "errorCode":-7,"errorMsg":""
        }

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_res = create_calen_note()
        self.body['rows']='@#@@@@'
        calen_res = get_calen_note(data=self.body)

        self.assertEqual(500, calen_res.status_code, msg='return code error')
        CheckMethod().output_check(expectBase, calen_res.json())