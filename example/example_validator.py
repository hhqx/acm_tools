import random

from acm_tools import *

question_str = """
Input:
1 2 3 4 5


Output:
15

Input:
1 1 1 1 1
Output:
5


"""
load_test_str(question_str)


# 对拍器, 加在被测试函数上的装饰器, @use_truth_to_validate(func_truth)
def use_truth_to_validate(func_truth):
    def decorator(func_validate):
        def func(*args, **kwargs):
            result = func_validate(*args, **kwargs)
            truth = func_truth(*args, **kwargs)
            assert result == truth, \
                f"Validation failed. \nInput: {args} \n Output: {result} \n Expected: {truth}"
            return func_validate(*args, **kwargs)
        return func
    return decorator


#### START ####

def truth(arr):
    return sum(arr)


@use_truth_to_validate(truth)
def func(arr):
    ans = 0
    for num in arr:
        ans += num
    return ans


def main():
    arr = list(map(int, input().split()))
    ret = func(arr)
    print(ret)


# using random data to test
import random
for iter in range(100):
    func([random.random() for _ in range(random.randint(1, 100))])

# read input and print results
import traceback
while True:
    try:
        main()
    except Exception as e:
        # 处理异常的代码块
        # traceback.print_exc()
        # if isinstance(e, AssertionError):
        #     traceback.print_exc()
        break

#### END ####
