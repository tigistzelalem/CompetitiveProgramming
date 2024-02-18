# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            new = head
            while new != curr:
                if new.val > curr.val:
                    new.val, curr.val = curr.val, new.val
                new = new.next
            curr = curr.next
        
        return head