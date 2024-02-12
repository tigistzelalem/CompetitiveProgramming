class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        ind = 0
        temp = self.head
        while temp:
            if ind == index:
                return temp.value
            ind += 1
            temp = temp.next

        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return 
        prev = self.head
        while prev.next:
            prev = prev.next
        prev.next = node



    def addAtIndex(self, index: int, val: int) -> None:

        if index <= 0:
            self.addAtHead(val)
            return 
            
        node = Node(val)
        ind = 0
        prev = self.head
        
        while prev:

            if ind == index -1:
                node.next = prev.next
                prev.next = node
                break

            ind += 1
            prev = prev.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 :
            if self.head:
                self.head = self.head.next
                
        ind = 0
        temp = self.head
        while temp:
            if ind == index - 1 and temp.next:
                temp.next = temp.next.next
                break
            ind += 1
            temp = temp.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)