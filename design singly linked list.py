class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, i: int) -> int:
        current = self.head
        index = 0

        while current:
            if index == i:
                return current.val
            current = current.next
            index += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, i: int) -> bool:
        if self.head is None:
            return False

        if i == 0:
            self.head = self.head.next
            return True

        current = self.head
        index = 0

        while current.next:
            if index + 1 == i:
                current.next = current.next.next
                return True

            current = current.next
            index += 1

        return False

    def getValues(self) -> list[int]:
        values = []
        current = self.head

        while current:
            values.append(current.val)
            current = current.next

        return values
