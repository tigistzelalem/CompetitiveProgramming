def has_cycle(head):
    if not head or not head.next:
        return False
    p1 = head
    p2 = head.next
    while p2:
        p2 = p2.next
        if p2:
            p2 = p2.next
        if not p2:
            return False
        p1 = p1.next
        if p1 == p2:
            return True
