"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"ListNode: [value={self.value}, prev={self.prev}, next={self.next}]"

    def __str__(self):
        return f"[{self.value}]"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        output = "DoublyLinkedList: [ "

        cur_node = self.head
        while cur_node is not None:
            output += " <=> " if cur_node.prev else ""
            output += f"{cur_node}"
            cur_node = cur_node.next

        return output + " ]"

    def __str__(self):
        output = ""

        cur_node = self.head
        while cur_node is not None:
            output += " <=> " if cur_node.prev else ""
            output += f"{cur_node}"
            cur_node = cur_node.next

        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head:
            cur_node = self.head
            cur_node.insert_before(value)
            self.head = cur_node.prev
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

        self.length += 1

    """Removes the given node, and returns the value of the 
    removed Node."""

    def _remove_node(self, node):
        if node is None:
            return None

        rtn_val = node.value
        self.delete(node)
        return rtn_val

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        return self._remove_node(self.head)

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.tail:
            cur_node = self.tail
            cur_node.insert_after(value)
            self.tail = cur_node.next
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        return self._remove_node(self.tail)

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node.next is None:
            self.tail = node.prev

        node.delete()
        node.next = self.head
        self.head.prev = node
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node.prev is None:
            self.head = node.next

        node.delete()
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node is None:
            return

        if node.prev is None:
            self.head = node.next
        if node.next is None:
            self.tail = node.prev

        node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        cur_node = self.head

        max_val = cur_node.value
        while cur_node.next:
            if cur_node.next.value > max_val:
                max_val = cur_node.next.value
            cur_node = cur_node.next

        return max_val
