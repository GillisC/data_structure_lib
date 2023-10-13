
class ListNode:

    def __init__(self, data):
        self.data = data
        self.next: ListNode = None

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_next(self, node):
        self.next = node

    def set_data(self, data):
        self.data = data

    def __str__(self):
        return f"{self.data}"
