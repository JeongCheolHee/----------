import sys
sys.path.append('c:\\Users\\USER\\structure-3')


from list.src.model.listnode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def get_start_node(self):
        if self.__numItems == 0:
            return None
        return self.__tail.next.next

    def insert(self, i: int, newItem):
        if not (0 <= i <= self.__numItems):
            print("Index out of bounds")
            return

        newNode = ListNode(newItem, None)
        if i == 0:
            newNode.next = self.__tail.next.next
            self.__tail.next.next = newNode
            if self.__numItems == 0:
                self.__tail = newNode
        else:
            prev = self.getNode(i - 1)
            newNode.next = prev.next
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
        self.__numItems += 1

    def append(self, newItem):
        self.insert(self.__numItems, newItem)

    def pop(self, i=None):
        if self.__numItems == 0:
            return None

        if i is None or i == -1 or i >= self.__numItems:
            i = self.__numItems - 1

        if i == 0:
            removedItem = self.__tail.next.next.item
            self.__tail.next.next = self.__tail.next.next.next
            if self.__numItems == 1:
                self.__tail = self.__tail.next                      # Reset to dummy when list becomes empty
        else:
            prev = self.getNode(i - 1)
            removedItem = prev.next.item
            prev.next = prev.next.next
            if i == self.__numItems - 1:
                self.__tail = prev
        self.__numItems -= 1
        return removedItem

    def getNode(self, i: int):
        if i >= self.__numItems:
            return None
        current = self.__tail.next.next
        for _ in range(i):
            current = current.next
        return current

    def printList(self):
        current = self.get_start_node()
        for _ in range(self.__numItems):
            print(current.item, end=' ')
            current = current.next
        print()

    def __iter__(self):
        self.current = self.get_start_node()
        self.count = 0
        return self

    def __next__(self):
        if self.count == self.__numItems:
            raise StopIteration
        item = self.current.item
        self.current = self.current.next
        self.count += 1
        return item

    def sort(self):
        if self.__numItems > 1:
            items = []
            current = self.get_start_node()
            for _ in range(self.__numItems):
                items.append(current.item)
                current = current.next
            items.sort()

            self.clear()                            # Clear the list and reinsert items in sorted order
            for item in items:
                self.append(item)

    def clear(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0
