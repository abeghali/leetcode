from typing import Optional

l1_list = [4,3,1,2]
l2_list = [1,6,2,5]

# output = 2134 + 5261 = 7395 = [5, 9, 3, 7]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Beginning of solution

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_list_values = []
        l2_list_values = []

        current = l1
        while current:
            l1_list_values.append(str(current.val))
            current = current.next

        current = l2
        while current:
            l2_list_values.append(str(current.val))
            current = current.next
        
        l1_int = int("".join([str(num) for num in l1_list_values[::-1]]))
        l2_int = int("".join([str(num) for num in l2_list_values[::-1]]))
        new_num = l1_int + l2_int
        new_list = [int(x) for x in str(new_num)]

        dummy_head = ListNode()
        current = dummy_head
        for num in new_list[::-1]:
            current.next = ListNode(num)
            current = current.next

        return dummy_head.next

# End of solution

def make_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

l1 = make_linked_list(l1_list)
l2 = make_linked_list(l2_list)

def print_linked_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))

solution = Solution()
output = solution.addTwoNumbers(l1, l2)
print_linked_list(output)