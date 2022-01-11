# -*- coding: utf-8 -*-
# time:2022/1/6 22:04
# author：ZL
# File:example02.py
# Project:Leetcode
# Software:PyCharm

"""
用指针实现有序数组中的二分查找
"""

numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
left, right = 0, len(numbers) - 1
search = int(input("Enter a number to search:"))
ans = 0

while right - left > 1:
    mid = (left + right) // 2

    if search < numbers[mid]:
        right = mid
    elif search > numbers[mid]:
        left = mid + 1
    elif search == numbers[mid]:
        ans = mid
        break
else:
    if search == numbers[left]:
        ans = left
    else:
        ans = -1
print(ans)
