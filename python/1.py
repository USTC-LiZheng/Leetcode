# -*- coding: utf-8 -*-
# time:2021/11/15 20:45
# author：ZL
# File:1.py
# Project:Date_structure
# Software:PyCharm

# 1、两数之和
"""
题目：
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
输入：nums = [3,2,4], target = 6
输出：[1,2]
输入：nums = [3,3], target = 6
输出：[0,1]
"""
from typing import List
# my


class Solution:
    @staticmethod
    def twosum(alist, target):
        for i in range(len(alist)):
            for j in range(i + 1, len(alist)):
                if alist[i] + alist[j] == target:
                    return [i, j]


# hash


class Solution_hash:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:  # # ->List[int] 表示该函数的返回值是List[int]类型的
        records = dict()
        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]  # 如果存在就返回字典记录索引和当前索引


if __name__ == '__main__':
    nums_test = [2, 7, 11, 15]
    target_test = 9
    Solution.twosum(nums_test, target_test)
    print(Solution.twosum(nums_test, target_test))
