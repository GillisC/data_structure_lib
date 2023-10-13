from typing import Iterator
from list_node import ListNode
from linked_list_iterator import LinkedListIterator

"""A linked list keeps a reference to the head of the array and every node keeps a reference to the next node"""
class LinkedList:
    size: int

    def __init__(self):
        self.head: ListNode = None
        self.size = 0

    """Appends the element to the back of the linked list"""
    def add(self, item):
        new_node = ListNode(item)
        if self.size < 1:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    """Removes the node at the specified index"""
    """Returns true if a value was removed, false if index was out of range"""
    def remove_node(self, index):
        curr_index = 0
        if index == 0:
            self.head = self.head.get_next()
        for data in self.__iter__():
            if curr_index + 1 == index:
                first_node = data
                third_node = data.get_next().get_next()
                first_node.set_next(third_node)
                self.size -= 1
                return True
            curr_index += 1
        return False

    """Changes the data of the node at the specified index"""
    """Returns true if data was modified, false if index was out of range"""
    def set_data_at_node(self, data, index: int) -> bool:
        current_index = 0
        for item in self.__iter__():
            if current_index == index:
                item.set_data(data)
                return True
            current_index += 1
        return False

    def contains(self, in_data) -> bool:
        for data in self.__iter__():
            if in_data is data.get_data():
                return True
        return False

    """Clears the whole list"""
    def clear(self):
        self.head = None
        self.size = 0

    def __iter__(self) -> Iterator[ListNode]:
        return LinkedListIterator(self.head)

    def __str__(self):
        contents: list[ListNode] = [item for item in self.__iter__()]
        output = ""
        for item in contents:
            output += f"{item.data} -> "
        s = slice(0, -4)  # Removes the last arrow
        return output[s]


def main():
    linked_list = LinkedList()
    for i in range(0, 5):
        linked_list.add(i)

    print(linked_list)

    linked_list.remove_node(4)
    print("\n")

    print(linked_list)

    num: str = "test"
    num.__hash__()
    print(num.__hash__())


if __name__ == "__main__":
    main()
