# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length1 = 0
        node1 = headA
        while node1:
            length1 += 1
            node1 = node1.next

        length2 = 0
        node2 = headB
        while node2:
            length2 += 1
            node2 = node2.next

        longest_node = headA if length1 > length2 else headB
        shortest_node = headA if length1 <= length2 else headB
        difference = abs(length1 - length2)

        while difference > 0:
            longest_node = longest_node.next
            difference -= 1
        
        while shortest_node:
            if shortest_node == longest_node:
                return shortest_node
            shortest_node = shortest_node.next
            longest_node = longest_node.next