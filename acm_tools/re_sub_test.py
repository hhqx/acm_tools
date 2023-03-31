import re

from typing import List


def sub_string_by_list(string: str, old_list: List[str], new_list: List[str]):
    """
    用正则批量替换string, old_list[0] 替换为 new_list[0] ...
    """
    # 拼接正则表达式和替换模板
    regex = '|'.join(map(re.escape, old_list))
    template = lambda match: new_list[old_list.index(match.group(0))]
    new_text = re.sub(regex, template, string)
    return new_text


if __name__ == '__main__':
    old_list = ['old1', 'old2', 'old3']
    new_list = ['new1', 'new2', 'new3']
    # 进行替换
    text = 'This is old1 text, and this is old2 text.'
    new_text = sub_string_by_list(text, old_list, new_list)
    print(new_text)
