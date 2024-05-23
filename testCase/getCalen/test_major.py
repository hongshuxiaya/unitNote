import unittest
from copy import deepcopy
from business.getIndexNote import get_calen_list, get_calen_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_calen_note
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
        """查看日历便签主流程"""
        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res=create_calen_note()
        calen_res=get_calen_note()

        self.assertEqual(200, calen_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase)
        expect['webNotes'][0]['noteId'] = create_res[2]['noteId']
        expect['webNotes'][0]['star'] = create_res[2]['star']
        CheckMethod().output_check(expect, calen_res[0])
