# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return head

            # Swap nodes in pairs
        previous = None
        current = head
        while current and current.next:
                next_pair = current.next.next
                second = current.next
                second.next = current
                current.next = next_pair
                if previous:
                    previous.next = second
                else:
                    head = second
                previous = current
                current = next_pair

        return head