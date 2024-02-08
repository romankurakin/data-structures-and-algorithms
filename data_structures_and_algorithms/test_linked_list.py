from linked_list import LinkedList, OrderedList


def test_linked_list_append_and_get():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.get(0) == 1
    assert ll.get(1) == 2


def test_linked_list_prepend():
    ll = LinkedList()
    ll.prepend(2)
    ll.prepend(1)
    assert ll.get(0) == 1
    assert ll.get(1) == 2


def test_linked_list_delete():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(1)
    assert ll.search(1) is False
    assert ll.get(0) == 2


def test_linked_list_search():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.search(2) is True
    assert ll.search(3) is False


def test_linked_list_reverse():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.reverse()
    assert ll.get(0) == 2
    assert ll.get(1) == 1


def test_linked_list_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(1)
    assert ll.length() == 1


def test_ordered_list_add_and_get():
    ol = OrderedList()
    ol.add(3)
    ol.add(1)
    ol.add(2)
    assert ol.get(0) == 1
    assert ol.get(1) == 2
    assert ol.get(2) == 3


def test_ordered_list_max_min():
    ol = OrderedList()
    ol.add(1)
    ol.add(3)
    ol.add(2)
    assert ol.max() == 3
    assert ol.min() == 1


def test_ordered_list_search():
    ol = OrderedList()
    ol.add(1)
    ol.add(3)
    ol.add(2)
    assert ol.search(2) is True
    assert ol.search(4) is False


def test_ordered_list_delete():
    ol = OrderedList()
    ol.add(1)
    ol.add(3)
    ol.add(2)
    ol.delete(3)
    assert ol.search(3) is False
    assert ol.get(1) == 2
    assert ol.length() == 2


def test_ordered_list_length():
    ol = OrderedList()
    ol.add(1)
    ol.add(3)
    ol.add(2)
    ol.delete(2)
    assert ol.length() == 2


def test_print_list(capsys):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
    captured = capsys.readouterr()
    assert captured.out == "1 -> 2 -> 3\n"
