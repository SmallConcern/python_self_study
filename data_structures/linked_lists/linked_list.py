

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if self.head:
            next_node = self.head
            while next_node.next_node:
                next_node = next_node.next_node
            next_node.next_node = node
        else:
            self.head = node

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next_node
        return None

    def delete(self, data):
        previous = None
        node = self.head
        while node:
            if node.data == data:
                break
            else:
                previous = node
                node = node.next_node
        if not node:
            return False
        if not previous:
            self.head = node.next_node
        else:
            previous.next_node = node.next_node
        return True

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev

    def reverse_into_new(self, node):
        import copy
        new_ll = copy.deepcopy(node)
        current = new_ll.head
        prev = None
        while current:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        new_ll.head = prev
        return new_ll

    def _reverse_r(self, curr, prev):
        if curr.next_node is None:
            self.head = curr
            curr.next_node = prev
            return
        next = curr.next_node
        curr.next_node = prev
        self._reverse_r(next, curr)

    def reverse_r(self):
        self._reverse_r(self.head, None)


def get_linked_list_data_dump(linked_list):
    data = []
    node = linked_list.head
    while node:
        data.append(node.data)
        node = node.next_node
    return ' '.join(data)

def generate_test_linked_list():
    ll = LinkedList(Node("foo"))
    ll.append(Node("bar"))
    ll.append(Node("hello"))
    ll.append(Node("world"))
    return ll

def test_linked_list_reverse():
    ll = generate_test_linked_list()
    assert get_linked_list_data_dump(ll) == "foo bar hello world"
    ll.reverse()
    assert get_linked_list_data_dump(ll) == "world hello bar foo"
    ll.reverse_r()
    assert get_linked_list_data_dump(ll) == "foo bar hello world"
    ll2 = ll.reverse_into_new(ll)
    assert get_linked_list_data_dump(ll2) == "world hello bar foo"
    assert get_linked_list_data_dump(ll) == "foo bar hello world"

def test_linked_list_delete():
    ll = generate_test_linked_list()
    assert ll.delete("bar")
    assert get_linked_list_data_dump(ll) == "foo hello world"
    assert ll.delete("world")
    assert get_linked_list_data_dump(ll) == "foo hello"
    assert ll.delete("foo")
    assert get_linked_list_data_dump(ll) == "hello"
    assert not ll.delete("dfasdfas")
    assert get_linked_list_data_dump(ll) == "hello"
    ll = LinkedList()
    assert not ll.delete("foo")

def test_linked_list_search():
    ll = generate_test_linked_list()
    assert ll.search("foo")
    assert ll.search("hello")
    assert not ll.search("kadsjflasj")
    ll = LinkedList()
    assert not ll.search("foo")

def test_linked_list_creation():
    ll = LinkedList()
    assert ll
    assert not ll.head
    ll = LinkedList(Node("foo"))
    assert ll.head.data == "foo"

def test_linked_list_append():
    ll = LinkedList()
    ll.append(Node("foo"))
    ll.append(Node("bar"))
    assert ll.head.next_node.data == "bar"
    ll.append(Node("hello"))
    ll.append(Node("world"))
    assert get_linked_list_data_dump(ll) == "foo bar hello world"

def test_node_creation():
    n = Node()
    assert n
    assert not n.data
    assert not n.next_node
    n = Node("foo")
    assert n.data == "foo"
    n2 = Node("bar")
    n.next_node = n2
    assert n.next_node == n2