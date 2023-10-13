from typing import Iterator

from linked_list import LinkedList
from linked_list_iterator import LinkedListIterator
from list_node import ListNode

"""Queue implemented as a linked list, FIFO"""


class Queue:

    def __init__(self):
        self.head = None
        self.size = 0

    """Adds the item to the back of the queue"""
    def enqueue(self, item):
        new_node = ListNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.size += 1

    """Removes and returns the first item in the queue"""
    def dequeue(self) -> ListNode:
        if self.is_empty():
            raise Exception("Queue is empty, no element to be retrieved")
        removed_node = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return removed_node

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
    queue = Queue()
    empty_queue = Queue()
    empty_queue.dequeue()
    for i in range(0, 5):
        queue.enqueue(i)

    print(queue)
    queue.dequeue()
    print("\n")

    print(queue)
    print(queue.contains(1))


if __name__ == "__main__":
    main()
