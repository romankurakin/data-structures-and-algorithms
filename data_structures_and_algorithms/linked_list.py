from typing import Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional["Node"] = None


class BaseList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

    def print_list(self):
        """Print the entire list in a readable format."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements))

    def length(self):
        """Return the length of the list."""
        return self.size

    def reverse(self):
        """Reverse the list in place."""
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def get(self, index):
        """Return the element at the given index."""
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                raise IndexError("Index out of range")
            current_node = current_node.next
        return current_node.data

    def delete(self, data):
        """Delete the first occurrence of the given element from the list."""
        current_node = self.head
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is None:
            self.head = current_node.next
        elif current_node:
            prev_node.next = current_node.next
        self.size -= 1

    def search(self, target):
        """Search for a target value in the list.
        Returns True if the target is found, and False otherwise."""
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            current_node = current_node.next
        return False


class LinkedList(BaseList):
    def __init__(self):
        super().__init__()
        self.tail: Optional[Node] = None

    def append(self, data):
        """Append an element to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """Prepend an element to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1


class OrderedList(BaseList):
    def add(self, data):
        """Add an element to the list while maintaining sorted order."""
        new_node = Node(data)
        current_node = self.head
        prev_node = None
        while current_node and current_node.data < data:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is None:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node.next = new_node
            new_node.next = current_node
        self.size += 1

    def max(self):
        """Return the maximum element in the list."""
        if self.head is None:
            return None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node.data

    def min(self):
        """Return the minimum element in the list."""
        if self.head is None:
            return None
        return self.head.data

    def search(self, target):
        """Search for a target value in the ordered list.
        Stops the search early if the target value is not found before surpassing the target.
        Returns True if the target is found, and False otherwise."""
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            elif current_node.data > target:
                return False
            current_node = current_node.next
        return False
