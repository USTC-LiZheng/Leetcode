# -*- coding: utf-8 -*-
# time:2022/1/9 19:47
# author：ZL
# File:example03.py
# Project:Leetcode
# Software:PyCharm
"""
正序输出双链表
"""

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]

head = ListLeft.index(-1)
print(ListValue[head])
Next = ListRight[head]

while Next > -1:
    print(ListValue[Next])
    Next = ListRight[Next]