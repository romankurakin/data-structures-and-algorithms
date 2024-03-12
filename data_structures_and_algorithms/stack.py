class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return self.items == []

    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self):
        """Remove an item from the stack."""
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack."""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
