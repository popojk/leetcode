"""
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(N)
        Space: O(1)
        """
        # init a dummy node to store result
        dummy = ListNode()
        # init a res node to store the head node of dummy node in order to return answer
        res = dummy
        # init total, carry variable to store result in current node count
        total, carry = 0, 0
        # iterate while l1 or l2 or carry != None or 0
        while l1 or l2 or carry:
            # total init with carry
            total = carry
            # if l1 or l2 is not none, calculate total and move forward
            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            # init var num by total%10 where num represent the num in new node
            num = total % 10
            # update carry by total//10
            carry = total // 10
            # make new node to dummy.next
            dummy.next = ListNode(val=num)
            # move dummy to dummy.next
            dummy = dummy.next
        # return res.next as answer
        return res.next
