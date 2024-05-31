import time
import unittest
from copy import deepcopy

from business.getIndexNote import get_index_list, get_index_note, get_calen_list, get_calen_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_recyc_note, clear_note
from business.createNoteData import create_common_note, create_calen_note
from common.checkOutput import CheckMethod
from common.readYaml import data_config


@class_case_log
class TestGetCalenMajor(unittest.TestCase):
    body = data_config()['getcalen_note']['body']

    def testCase01_get_NOnote_handle(self):
        """获取日历便签无数据"""
        expectBase = {"responseTime":0,"webNotes":[]}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        index_res = get_calen_note()
        self.assertEqual(200, index_res[1].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, index_res[1].json())


    def testCase02_get_morestartnote_handle(self):
        """获取日历便签索引超过时间"""
        expectBase = {"responseTime":0,"webNotes":[]}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_calen_note()
        startTime = str(time.time() * 1000)[:-5]
        self.body['startTime']=int(startTime)
        index_res = get_calen_note(data=self.body)
        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, index_res[1].json())

    def testCase03_get_onlynote_handle(self):
        """获取日历便签只有普通便签数据"""
        expectBase = {"responseTime":0,"webNotes":[]}

        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_common_note()

        index_res = get_calen_note()
        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, index_res[1].json())

    def testCase04_get_twonote_handle(self):
        """获取日历便签多个日历便签"""
        expectBase = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": int,
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
                },
                {
                    "noteId": str,
                    "createTime": int,
                    "star": int,
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

        create_res1=create_calen_note()
        create_res2 = create_calen_note()

        index_res = get_calen_note()

        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        expect = deepcopy(expectBase)
        expect['webNotes'][0]['noteId'] = create_res2[2]['noteId']

        expect['webNotes'][1]['noteId'] = create_res1[2]['noteId']

        CheckMethod().output_check(expectBase, index_res[0])