"""
Tests for LeetCode Problem 2: Add Two Numbers
"""

from solution import ListNode, Solution


def list_to_linked_list(values: list[int]) -> ListNode | None:
    """Helper function to convert a list to a linked list."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """Helper function to convert a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem."""

    def test_example_1(self):
        """Test case: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)"""
        solution = Solution()
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]

    def test_example_2(self):
        """Test case: [0] + [0] = [0]"""
        solution = Solution()
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_example_3(self):
        """Test case: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]"""
        solution = Solution()
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

    def test_different_lengths(self):
        """Test case: Lists of different lengths"""
        solution = Solution()
        l1 = list_to_linked_list([1, 8])
        l2 = list_to_linked_list([0])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [1, 8]

    def test_with_carry(self):
        """Test case: Addition with carry"""
        solution = Solution()
        l1 = list_to_linked_list([9, 9])
        l2 = list_to_linked_list([1])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0, 0, 1]

    def test_single_digit(self):
        """Test case: Single digit addition"""
        solution = Solution()
        l1 = list_to_linked_list([5])
        l2 = list_to_linked_list([5])
        result = solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0, 1]
