# -*- coding: utf-8 -*-
# time:2021/11/22 21:35
# author：ZL
# File:9.py
# Project:Date_structure
# Software:PyCharm
"""
题目：给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例：输入：x = 121  输出：true
     输入：x = -121  输出：false
     解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        a = str(x)
        b = a[::-1]
        if a == b:
            print(True)
            return True
        else:
            print(False)
            return False


"""
进阶解法---巧妙解法
直观上来看待回文数的话，就感觉像是将数字进行对折后看能否一一对应。所以这个解法的操作就是 取出后半段数字进行翻转。
这里需要注意的一个点就是由于回文数的位数可奇可偶，所以当它的长度是偶数时，它对折过来应该是相等的；当它的长度是奇数时，那么它对折过来后，有一个的长度需要去掉一位数（除以 10 并取整）。
具体做法如下：
每次进行取余操作 （ %10），取出最低的数字：y = x % 10
将最低的数字加到取出数的末尾：revertNum = revertNum * 10 + y
每取一个最低位数字，x 都要自除以 10
判断 x 是不是小于 revertNum ，当它小于的时候，说明数字已经对半或者过半了
最后，判断奇偶数情况：如果是偶数的话，revertNum 和 x 相等；如果是奇数的话，最中间的数字就在revertNum 的最低位上，将它除以 10 以后应该和 x 相等。
"""


class Solution1:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
        if x == revertedNumber or x == revertedNumber // 10:
            return True
        else:
            return False


if '__name__' == '__main__':
    print(Solution1.isPalindrome(121))
