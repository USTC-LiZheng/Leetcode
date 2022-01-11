# -*- coding: utf-8 -*-
# time:2022/1/4 20:59
# author：ZL
# File:35.py
# Project:Leetcode
# Software:PyCharm
from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return right + 1


