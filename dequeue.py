from typing import Iterator

from linked_list_iterator import LinkedListIterator
from list_node import ListNode


class Deque:

    def __init__(self):
        self.head = None
        self.size = 0

    """Adds the item to the front of the queue"""
    def enqueue_front(self, item):
        new_node = ListNode(item)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    """Adds the item to the back of the queue"""
    def enqueue_back(self, item):
        new_node = ListNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.size += 1

    """Removes and returns the item at the front of the queue"""
    def dequeue_front(self) -> ListNode:
        if self.is_empty():
            raise Exception("Dequeue is empty, no element to be retrieved")
        removed_node = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return removed_node

    """Removes and returns the item at the back of the queue"""
    def dequeue_back(self):
        if self.is_empty():
            raise Exception("Dequeue is empty, no element to be retrieved")
        elif self.get_size() == 1:
            node_removed = self.head
            self.head = None
            self.size -= 1
            return node_removed
        else:
            current: ListNode = self.head
            while current.get_next().get_next() is not None:
                current = current.get_next()

            node_removed = current.get_next()
            current.set_next(None)
            self.size -= 1
            return node_removed


    def get_first(self) -> ListNode:
        if self.is_empty():
            raise Exception("Queue is empty, can't retrieve the first element")
        return self.head

    def get_last(self) -> ListNode:
        if self.is_empty():
            raise Exception("Queue is empty, can't retrieve the last element")
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        return current

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return True if self.head is None else False

    def contains(self, item) -> bool:
        for node in self.__iter__():
            if node.get_data() is item:
                return True
        return False

    def clear(self) -> None:
        self.head = None
        self.size = 0

    def __iter__(self) -> Iterator[ListNode]:
        return LinkedListIterator(self.head)

    def __str__(self):
        contents: list[ListNode] = [item for item in self.__iter__()]
        output = "["
        for item in contents:
            if item.next is None:
                output += f"{item.data}]"
            else:
                output += f"{item.data}, "
        return output

def main():
    pass


if __name__ == "__main__":
    main()