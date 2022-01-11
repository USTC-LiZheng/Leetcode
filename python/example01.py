# -*- coding: utf-8 -*-
# time:2022/1/6 21:53
# author：ZL
# File:example01.py
# Project:Leetcode
# Software:PyCharm

"""
用指针合并两个有序数组
"""
arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
ans = arr1.copy()

ind = 0
for i in range(0, len(arr2)):
    while ind < len(arr1):
        if arr2[i] <= arr1[ind]:
            ans.insert(ind + i, arr2[i])
            break
        else:
            ans.append(arr1[ind])
            ind += 1
else:
    ans = ans + arr2[i:]

print(ans)