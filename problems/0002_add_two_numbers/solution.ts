/**
 * LeetCode Problem 2: Add Two Numbers
 *
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 */

/**
 * Definition for singly-linked list.
 */
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * Add two numbers represented as linked lists.
 *
 * @param l1 - First linked list (digits in reverse order)
 * @param l2 - Second linked list (digits in reverse order)
 * @returns Sum as a linked list (digits in reverse order)
 *
 * Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
 * Space Complexity: O(max(m, n)) for the result list
 */
function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const dummyHead = new ListNode(0);
  let current = dummyHead;
  let carry = 0;

  while (l1 !== null || l2 !== null || carry !== 0) {
    // Get values from current nodes (0 if node is null)
    const val1 = l1 !== null ? l1.val : 0;
    const val2 = l2 !== null ? l2.val : 0;

    // Calculate sum and carry
    const total = val1 + val2 + carry;
    carry = Math.floor(total / 10);
    const digit = total % 10;

    // Create new node with the digit
    current.next = new ListNode(digit);
    current = current.next;

    // Move to next nodes
    l1 = l1 !== null ? l1.next : null;
    l2 = l2 !== null ? l2.next : null;
  }

  return dummyHead.next;
}

export { ListNode, addTwoNumbers };
