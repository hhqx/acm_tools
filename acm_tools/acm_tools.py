import re
from builtins import print as print_std
from builtins import print as sprint
from builtins import input as input_std
from collections import deque
import io

from .rich_tools import display_diff_table
from .re_sub_test import sub_string_by_list

__all__ = ['input', 'print', 'load_test_str', 'dprint', 'print_std', 'sprint']

STD_IN = """"""
STD_OUT = """"""
str_in = deque()
std_out = deque()

io_std = io.StringIO()
io_debug = io.StringIO()

Test_Case = deque()


def load_stdin(stdin):
    str_in.extend([row for row in stdin.split('\n') if row])


def load_test_str(test_str: str):
    global STD_IN, STD_OUT
    # 批量替换 test_str 中的字符
    test_str = sub_string_by_list(
        test_str,
        ["样例输入", "样例输出", "输入:", "输入：", "输出:", "输出：", ],
        ["Input:", "Output:", "Input:", "Input:", "Output:", "Output:", ]
    )
    # 定义正则表达式
    pattern = r'^Input:([\s\S]*?)Output:([\s\S]*?)(\Z|(?=Input)|(?=#)|(?=\n[\u4e00-\u9fa5]))'
    matches = re.findall(pattern, test_str, re.MULTILINE)
    cases = []
    for m in matches:
        sin, sout = m[:2]
        cases.append([sin, sout])
        Test_Case.append([sin, sout])
        # print_std(sin, sout)
    assert len(Test_Case), "'test_str: str' does not contain any test case."
    STD_IN, STD_OUT = map(lambda x: x.strip(), Test_Case.popleft())
    std_out.append(STD_OUT)
    load_stdin(STD_IN)


# def load_test_case(stdin, stdout):
#     global STD_IN, STD_OUT
#     STD_IN = stdin
#     STD_OUT = stdout

def pop_new_case():
    stdin, STD_OUT = map(lambda x: x.strip(), Test_Case.popleft())
    std_out.append(STD_OUT)
    return stdin


def exist_case():
    return len(Test_Case) != 0


def input(*args, **kwargs):
    if len(str_in):
        return str_in.popleft()
    else:
        assert 0, 'no more input.'
        input_std(*args, **kwargs)


def print_debug(*args, **kwargs):
    print_std(*args, file=io_debug, **{k: v for k, v in kwargs.items() if k != 'file'})


dprint = print_debug

case_idx = 0
err_cnt = 0
is_correct = False


def print(*args, **kwargs):
    global io_std, io_debug
    global case_idx
    global err_cnt, is_correct
    print_std(*args, file=io_std, **{k: v for k, v in kwargs.items() if k != 'file'})
    # print_std(*args, **kwargs)
    is_end = len(str_in) == 0
    if exist_case() and is_end:
        load_stdin(pop_new_case())
    if is_end:
        case_idx += 1
        # print_std(f'Case {case_idx}:')
        STD_OUT = std_out.popleft()
        # 清除缓存区中的内容
        info_debug = io_debug.getvalue().strip()
        # io_debug.flush()
        io_debug = io.StringIO()

        # # if info_debug:
        # print_std('Debug Info:')
        # print_std(info_debug)

        # 清除std缓存区中的内容
        output = io_std.getvalue().strip()
        # io_std.truncate(0)
        # io_std.flush()
        io_std = io.StringIO()

        # # if STD_OUT:
        # print_std('Output:')
        # print_std(output)
        # print_std('Target:')
        # print_std(STD_OUT)
        output, target = [output.splitlines(), STD_OUT.splitlines()]
        is_correct = output == target
        err_cnt += not is_correct
        display_diff_table(
            info_debug.splitlines(), outputs=output, targets=target,
            title=f'Case {case_idx}', caption=f"Correct Count: {case_idx - err_cnt}/{case_idx}",
            caption_style="bold green" if err_cnt == 0 else "bold red",
        )
