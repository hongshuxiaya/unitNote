import os
import unittest

from BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
Env = "Online"
if __name__ == '__main__':
    run_pattern = 'test_*.py'
    suit = unittest.TestLoader().discover('./testCase', pattern=run_pattern)

    result = BeautifulReport(suit)
    result.report(filename='report.html', description='测试报告')
