import unittest
from copy import deepcopy
from business.getIndexNote import get_index_list, get_calen_list, get_noteIndex_data
from common.logCreate import class_case_log
from business.clearNoteData import clear_note, clear_recyc_note
from business.createNoteData import create_common_note, create_calen_note, update_note
from common.checkOutput import CheckMethod



@class_case_log
class TestNoteMajor(unittest.TestCase):
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

    def testCase01_create_common_note_major(self):
        """上传普通便签主流程"""
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_res = create_common_note()

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_info)
        expect['infoVersion'] = 1
        CheckMethod().output_check(expect, create_res[0].json())

        self.assertEqual(200, create_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_content)
        expect['contentVersion'] = 1
        CheckMethod().output_check(expect, create_res[1].json())

        index_list = get_index_list()
        self.assertIn(str(create_res[2]['noteId']), index_list, msg='noteId not found')

    def testCase02_create_calen_note_major(self):
        """上传日历便签主流程"""
        calen_list = get_calen_list()
        for note_id in calen_list:
            clear_note(note_id)
        clear_recyc_note(calen_list)

        create_res = create_calen_note()

        self.assertEqual(200, create_res[0].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_info)
        expect['infoVersion'] = 1
        CheckMethod().output_check(expect, create_res[0].json())

        self.assertEqual(200, create_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_content)
        expect['contentVersion'] = 1
        CheckMethod().output_check(expect, create_res[1].json())

        calen_list = get_calen_list()
        self.assertIn(str(create_res[2]['noteId']), calen_list, msg='noteId not found')

    def testCase03_update_common_note_major(self):
        """更新便签主流程"""
        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_res = create_common_note()
        note_data = get_noteIndex_data(create_res[2]['noteId'])

        update_res = update_note(note_data['noteId'], note_data['title'], note_data['summary'], create_res[2]['body'],
                                 note_data['contentVersion'])

        self.assertEqual(200, update_res[0].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_info)
        expect['infoVersion'] = note_data['infoVersion']+1
        CheckMethod().output_check(expect, update_res[0].json())

        self.assertEqual(200, update_res[1].status_code, msg='return code error')
        expect = deepcopy(self.expectBase_content)
        expect['contentVersion'] = note_data['contentVersion']+1
        CheckMethod().output_check(expect, update_res[1].json())

        index_list = get_index_list()
        self.assertIn(str(update_res[2]['noteId']), index_list, msg='noteId not found')

