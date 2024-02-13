# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.bin=''
        self.dec=0
        while head:
            self.bin += str(head.val)
            head=head.next
        count = 0
        val = int(self.bin)
        while count < len(self.bin):
            mod = val % 10
            self.dec +=  (mod * 2 **count)
            count += 1
            val //= 10


        return self.dec

        