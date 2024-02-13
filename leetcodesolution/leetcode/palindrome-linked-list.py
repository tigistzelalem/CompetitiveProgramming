# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        new_node = head
        prev_node = prev
        while new_node and prev_node:
            if new_node.val != prev_node.val:
                return False
            new_node = new_node.next
            prev_node = prev_node.next
        
        return True
        

