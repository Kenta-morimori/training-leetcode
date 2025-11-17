"""
LeetCode Problem 2: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(  # noqa: N802 - LeetCode method signature
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """
        Add two numbers represented as linked lists.

        Args:
            l1: First linked list (digits in reverse order)
            l2: Second linked list (digits in reverse order)

        Returns:
            Sum as a linked list (digits in reverse order)

        Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
        Space Complexity: O(max(m, n)) for the result list
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
