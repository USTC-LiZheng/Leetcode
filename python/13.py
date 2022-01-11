# -*- coding: utf-8 -*-
# time:2021/11/23 18:52
# author：ZL
# File:13.py
# Project:Date_structure
# Software:PyCharm


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = 0
        if len(s) == 1:
            a = d[s[0]]
            return a
        else:
            if s[len(s) - 2] == 'I' and s[len(s) - 1] == 'V':
                a = 4
            elif s[len(s) - 2] == 'I' and s[len(s) - 1] == 'X':
                a = 9
            elif s[len(s) - 2] == 'X' and s[len(s) - 1] == 'L':
                a = 40
            elif s[len(s) - 2] == 'X' and s[len(s) - 1] == 'C':
                a = 90
            elif s[len(s) - 2] == 'C' and s[len(s) - 1] == 'D':
                a = 400
            elif s[len(s) - 2] == 'C' and s[len(s) - 1] == 'M':
                a = 900
            else:
                for i in range(len(s) - 1, 0, -1):
                    a += d[s[i]]
            for i in range(len(s) - 3, 0, -1):
                a += d[s[i]]
            return a


class Solution1:
    def romanToInt(self, s):
        d = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        ln = len(s)
        for i in range(ln):
            if i < ln - 1 and d[s[i]] < d[s[i + 1]]:
                ret -= d[s[i]]
            else:
                ret += d[s[i]]
        return ret


if '__name__' == '__main__':
    a = Solution1.romanToInt('II')
    print(a)
