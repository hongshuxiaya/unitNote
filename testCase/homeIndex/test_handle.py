import unittest
from business.getIndexNote import get_index_list, get_index_note
from common.logCreate import class_case_log
from business.clearNoteData import clear_recyc_note, clear_note
from business.createNoteData import create_common_note, create_calen_note
from common.checkOutput import CheckMethod



@class_case_log
class TestGetMajor(unittest.TestCase):


    def testCase01_get_NOnote_handle(self):
        """获取首页便签无数据"""
        expectBase = {"responseTime":0,"webNotes":[]}

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        index_res = get_index_note()
        self.assertEqual(200, index_res[1].status_code, msg='return code error')

        CheckMethod().output_check(expectBase, index_res[1].json())


    def testCase02_get_morestartnote_handle(self):
        """获取首页便签索引超过数据"""
        expectBase = {"responseTime":0,"webNotes":[]}

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_common_note()

        index_res = get_index_note(startindex=str(1))
        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, index_res[1].json())

    def testCase03_get_onlycalennote_handle(self):
        """获取首页便签只有日历便签数据"""
        expectBase = {"responseTime":0,"webNotes":[]}

        index_list = get_index_list()
        for note_id in index_list:
            clear_note(note_id)
        clear_recyc_note(index_list)

        create_calen_note()

        index_res = get_index_note()
        self.assertEqual(200, index_res[1].status_code, msg='return code error')
        CheckMethod().output_check(expectBase, index_res[1].json())