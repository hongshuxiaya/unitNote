import unittest


class CheckMethod(unittest.TestCase):
    def output_check(self,expect,actual):
        """
        通用断言方法
        :param expect:
        :param actual:
        :return:
        """
        self.assertEqual(len(expect.keys()), len(actual.keys()), msg='keys len error!')
        for k, v in expect.items():
            self.assertIn(k, actual.keys(), msg=f'key:{k} not in response')
            if isinstance(v, type):
                self.assertEqual(v, type(actual[k]), msg=f'key:{k} type error')
            elif isinstance(v, list):
                self.assertEqual(len(v), len(actual[k]), msg='keys len error!')
                v.sort()
                actual[k].sort()
                for i in range(len(v)):
                    if isinstance(v[i],type):
                        self.assertEqual(v[i], type(actual[k][i]), msg=f'list key:{actual[k][i]} type error')
                    elif isinstance(v[i],dict):
                        self.output_check(v[i],actual[k][i])
                    else:
                        self.assertEqual(v[i], actual[k][i], msg=f'list key {actual[k][i]} value error!')
            elif isinstance(v,dict):
                self.output_check(v, actual[k])
            else:
                self.assertEqual(v, actual[k], msg=f'key:{k} value error')
