import unittest
from copy import deepcopy

import time

from business.getIndexNote import get_index_list, get_calen_list
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_common_note, create_calen_note, update_note
from common.checkOutput import CheckMethod

@class_case_log
class TestNotehandle(unittest.TestCase):
    expectBase_info = {
        "responseTime": int,
        "infoVersion": int,
        "infoUpdateTime": int
    }
    expectBase_content = {
        "responseTime": int,
        "contentVersion": int,
        "contentUpdateTime": int
    }

    def testCase01_update_common_note_handle(self):
        """普通便签转日历便签"""
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_res = create_common_note()
        noteid=create_res[2]['noteId']
        title=create_res[2]['title']
        summary=create_res[2]['summary']
        body=create_res[2]['body']
        localContentVersion=1
        remindTime=str(time.time() * 1000)[:-5]
        create_res = update_note(noteid, title, summary, body, localContentVersion, remindTime=remindTime, remindType=0)
        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_info)
        expect['infoVersion'] = 2
        CheckMethod().output_check(expect, create_res[0].json())

        self.assertEqual(200, create_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_content)
        expect['contentVersion'] = 2
        CheckMethod().output_check(expect, create_res[1].json())

    def testCase02_update_calen_note_handle(self):
        """日历便签转为普通便签"""
        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_calen_note()

        noteid = create_res[2]['noteId']
        title = create_res[2]['title']
        summary = create_res[2]['summary']
        body = create_res[2]['body']
        localContentVersion = 1

        create_res = update_note(noteid, title, summary, body, localContentVersion, remindTime=0, remindType=0)
        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_info)
        expect['infoVersion'] = 2
        CheckMethod().output_check(expect, create_res[0].json())

        self.assertEqual(200, create_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_content)
        expect['contentVersion'] = 2
        CheckMethod().output_check(expect, create_res[1].json())

    def testCase01_localversion_common_note_handle(self):
        """localcontentversion值错误"""
        expect={"errorCode":-1003,"errorMsg":"content version not equal!"}
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_res = create_common_note()
        noteid=create_res[2]['noteId']
        title=create_res[2]['title']
        summary=create_res[2]['summary']
        body=create_res[2]['body']
        localContentVersion=1
        update_note(noteid, title, summary, body, localContentVersion, remindTime=0, remindType=0)
        create_res = update_note(noteid, title, summary, body, localContentVersion, remindTime=0, remindType=0)


        self.assertEqual(412, create_res[1].status_code, msg='return code error')


        CheckMethod().output_check(expect, create_res[1].json())



