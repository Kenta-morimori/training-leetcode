"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

2つの空ではない連結リストが与えられます。これらの連結リストは、それぞれ非負の整数を表しており、各桁は逆順に格納され、各ノードは1つの数字を含んでいます。
この2つの数を足し合わせ、その合計を連結リストとして返してください。
ただし、2つの数には、0自身を除いて、先頭に0が含まれていないものとします。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        # どちらかのリストが残っているか，繰り上がりがある限り処理
        while l1 is not None or l2 is not None or carry:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            s = x + y + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next

"""
Note:
ListNodeを使う
"""
