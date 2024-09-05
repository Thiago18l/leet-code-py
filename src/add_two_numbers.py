from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, list_one: Optional[ListNode], list_two: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        result = current = ListNode()
        while list_one or list_two or carry:
            val_one = list_one.val if list_one else 0
            val_two = list_two.val if list_two else 0
            carry, val = divmod(val_one + val_two + carry, 10)
            current.next = ListNode(val)
            current = current.next
            list_one = list_one.next if list_one else None
            list_two = list_two.next if list_two else None
        return result.next
