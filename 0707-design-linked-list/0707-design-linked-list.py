class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        i = 0

        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1

        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        i = 0

        while current:
            if i == index - 1:
                newNode = Node(val)

                newNode.next = current.next
                current.next = newNode

                if newNode.next is None:
                    self.tail = newNode

                return

            current = current.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:

        if not self.head:
            return

        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return

        current = self.head
        i = 0

        while current.next:
            if i == index - 1:

                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                return

            current = current.next
            i += 1