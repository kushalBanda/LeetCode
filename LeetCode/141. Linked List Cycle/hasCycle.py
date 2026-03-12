from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False