import functools
import inspect
import os
from datetime import datetime
from main import DIR

from colorama import Fore


def info(text):
    stack = inspect.stack()
    formatted_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # 定义日志的输出时间
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"  # 当前执行文件名，跟行号
    content = f"[INFO]{formatted_time}-{code_path}>>{text}"
    print(Fore.LIGHTBLUE_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    log_file = DIR + "\\logs\\" + str_time + "_info.log"
    with open(log_file, "a",encoding='utf-8')as f:
        f.write(content + '\n')


def error(text):
    stack = inspect.stack()
    formatted_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # 定义日志的输出时间
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"  # 当前执行文件名，跟行号
    content = f"[INFO]{formatted_time}-{code_path}>>{text}"
    print(Fore.LIGHTRED_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    log_file = DIR + "\\logs\\" + str_time + "_er_info.log"
    with open(log_file, "a",encoding='utf-8')as f:
        f.write(content + '\n')


def case_log_init(func):
    @functools.wraps(func)  # 解决类装饰器的参数冲突问题
    def init(*args, **kwargs):
        class_name = args[0].__class__.__name__  # 获取类名
        method_name = func.__name__  # 获取方法名
        docstring = inspect.getdoc(func)  # 获取方法注释
        print(Fore.LIGHTBLUE_EX + '-------------------------------------------------------------------------')
        info(f"Class Name :{class_name}")
        info(f"Method Name :{method_name}")
        info(f"Test Description :{docstring}")
        func(*args, **kwargs)

    return init


def class_case_log(cls):
    """用例的日志装饰器级别"""
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith('testCase'):
            setattr(cls, name, case_log_init(method))
    return cls


if __name__ == '__main__':
    info('sdd')
