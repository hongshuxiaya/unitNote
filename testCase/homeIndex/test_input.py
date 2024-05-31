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
        """查看便签cookie不存在"""
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
        """查看便签cookieB用户"""
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

    def testCase03_get_note_Nonecookie_input(self):
        """查看便签cookie为None"""
        expectBase = {"errorCode":-2009,"errorMsg":""}
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_common_note()
        header = env_config()['headers']
        header['cookie'] = None
        calen_res = get_index_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase04_get_note_kongcookie_input(self):
        """查看便签cookie为kong"""
        expectBase = {"errorCode":-2009,"errorMsg":""}
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_common_note()
        header = env_config()['headers']
        header['cookie'] = ''
        calen_res = get_index_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())


    def testCase05_get_note_removecookie_input(self):
        """查看便签cookie缺失"""
        expectBase = {"errorCode":-2009,"errorMsg":""}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)
        create_common_note()
        header = env_config()['headers']
        header.pop('cookie')
        calen_res = get_index_note(headers=header)

        self.assertEqual(401, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    #-------------------startindex------------------------------------------
    def testCase06_get_note_kongstartIndex_input(self):
        """查看便签startIndex为kong"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res=create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/''/rows/99/notes'
        calen_res = get_index_note(url=url)


        self.assertEqual(404,calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase07_get_note_teshustartIndex_input(self):
        """查看便签startIndex为特殊字符"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/@#￥@/rows/99/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(404, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase08_get_note_xiaoshustartIndex_input(self):
        """查看便签startIndex为小数"""
        expectBase = {"errorCode":-7,"errorMsg":"参数类型错误！"}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url = 'https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/0.5/rows/99/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(500, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase09_get_note_fushustartIndex_input(self):
        """查看便签startIndex为负数"""
        expectBase = {"errorCode": -7, "errorMsg": "参数类型错误！"}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url = 'https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/-9/rows/99/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(500, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
    #-------------------userid-----------------------------------------
    def testCase10_get_note_konguserid_input(self):
        """查看便签usesrid为kong"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res=create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user//home/startindex/0/rows/99/notes'
        calen_res = get_index_note(url=url)


        self.assertEqual(404,calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase11_get_note_teshuuserid_input(self):
        """查看便签userid为特殊字符"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user/！@#￥/home/startindex/0/rows/99/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(404, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase12_get_note_Buserid_input(self):
        """查看便签userid为B用户"""
        expectBase = {"errorCode":-1011,"errorMsg":"user change!"}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url = 'https://note-api.wps.cn/v3/notesvr/user/609836667/home/startindex/0/rows/99/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(412, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
    # -------------------rows----------------------------------------
    def testCase13_get_note_kongrows_input(self):
        """查看便签rows为空"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}
        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res=create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/0/rows/''/notes'
        calen_res = get_index_note(url=url)


        self.assertEqual(404,calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase14_get_note_teshurows_input(self):
        """查看便签rows为特殊字符"""
        expectBase ={"timestamp":str,"status":int,"error":str,"message":str,"path":str}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url='https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/0/rows/@%###/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(404, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase15_get_note_xiaoshurows_input(self):
        """查看便签rows为小数"""
        expectBase = {"errorCode":-7,"errorMsg":"参数类型错误！"}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url = 'https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/0/rows/9.00/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(500, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())

    def testCase16_get_note_fushurows_input(self):
        """查看便签rows为负数"""
        expectBase = {"errorCode": -7, "errorMsg": "参数类型错误！"}

        calen_list = get_index_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_common_note()
        url = 'https://note-api.wps.cn/v3/notesvr/user/609836666/home/startindex/0/rows/-9/notes'
        calen_res = get_index_note(url=url)

        self.assertEqual(500, calen_res.status_code, msg='return code error')

        CheckMethod().output_check(expectBase, calen_res.json())
