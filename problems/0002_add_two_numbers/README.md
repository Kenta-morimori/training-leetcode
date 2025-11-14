# [2] Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Difficulty

- **Level**: Medium
- **Topics**: Linked List, Math, Recursion

## Examples

### Example 1:

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

### Example 2:

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3:

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Approach

### Initial Thoughts

This problem requires traversing two linked lists simultaneously while keeping track of the carry value from addition.

### Solution Strategy

1. Create a dummy head node to simplify list construction
2. Iterate through both lists simultaneously
3. Add corresponding values plus any carry from the previous addition
4. Create a new node with the sum modulo 10
5. Update carry as sum divided by 10
6. Continue until both lists are exhausted and carry is 0

### Time Complexity

- **Time**: O(max(m, n)) where m and n are the lengths of the two lists
- **Space**: O(max(m, n)) for the result list

## Code Implementation

See `solution.py` and `solution.ts` for implementations.

## Testing

Run tests with:

```bash
# Python
pytest test_solution.py

# TypeScript/JavaScript
npm test
```

## Notes

- Handle edge cases: different length lists, trailing carry
- Remember to create new nodes, don't modify input lists
- The dummy head pattern simplifies the logic
