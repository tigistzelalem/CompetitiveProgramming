# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        cur = head
        res = set()
        
        while cur:
            if cur.val in res:
                prev.next = cur.next
            else:
                res.add(cur.val)
                prev = cur
            cur = cur.next
        return head
                

                
            
    