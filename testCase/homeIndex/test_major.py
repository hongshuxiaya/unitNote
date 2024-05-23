import unittest
from copy import deepcopy
from business.getIndexNote import get_index_list, get_index_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_recyc_note, clear_note
from business.createNoteData import create_common_note
from common.checkOutput import CheckMethod



@class_case_log
class TestGetMajor(unittest.TestCase):
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


    def testCase01_get_note_major(self):
        """获取首页便签主流程"""
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_res = create_common_note()
        index_res = get_index_note()

        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, index_res[0])

