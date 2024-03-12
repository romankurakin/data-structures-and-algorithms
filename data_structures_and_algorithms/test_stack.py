from stack import Stack

def test_stack_is_empty():
    s = Stack()
    assert s.is_empty() is True

def test_stack_push():
    s = Stack()
    s.push(4)
    assert s.peek() == 4

def test_stack_pop():
    s = Stack()
    s.push("cat")
    s.push("dog")
    assert s.pop() == "dog"
    assert s.peek() == "cat"

def test_stack_size():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size() == 3
