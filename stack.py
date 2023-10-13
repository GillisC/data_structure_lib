from typing import Iterator

from linked_list_iterator import LinkedListIterator
from list_node import ListNode

"""Stack implemented as a linked list, FILO"""


class Stack:

    def __init__(self):
        self.head: ListNode = None
        self.size = 0

    def push(self, item):
        new_node = ListNode(item)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def pop(self) -> ListNode:
        if self.is_empty():
            raise Exception("Stack is empty, no element to be retrieved")
        removed_node = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return removed_node

    def peek(self) -> ListNode:
        return self.head

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
    stack = Stack()
    for i in range(0, 5):
        stack.push(i)

    print(stack)
    stack.pop()
    print(stack)

    assert stack.contains(1) is True



if __name__ == "__main__":
    main()
