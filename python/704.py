# -*- coding: utf-8 -*-
# time:2021/12/14 21:38
# author：ZL
# File:704.py
# Project:Leetcode
# Software:PyCharm
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1


