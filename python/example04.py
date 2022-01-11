# -*- coding: utf-8 -*-
# time:2022/1/11 13:35
# author：ZL
# File:example04.py
# Project:Leetcode
# Software:PyCharm

"""
两数之和
"""


def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]
        if target - m in dict:
            print((dict[target - m], i))
        dict[m] = i


if __name__ == '__main__':
    nums = [3, 4, 5, 7, 10, 1]
    print(twoSum(nums, 11))
