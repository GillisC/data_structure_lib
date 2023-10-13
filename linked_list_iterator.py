class LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.get_next()
            return item
