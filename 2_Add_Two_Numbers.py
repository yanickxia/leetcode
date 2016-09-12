# -*- coding:utf-8 -*-
from unittest import TestCase


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        ptr = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry /= 10
            if l1 != None or l2 != None or carry != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else:
                break
        return head
