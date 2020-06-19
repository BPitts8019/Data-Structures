class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"Node: [value={self.value}, next_node={self.next_node}]"


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def __repr__(self):
        return f"LinkedList: [Head: {self.head.value}, Tail: {self.tail.value}]"

    def __str__(self):
        output = ""
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.value} -> "
            cur_node = cur_node.next_node

        return output

    def __len__(self):
        return self.size

    def get_max(self):
        rtnVal = None

        if self.head != None:
            cur_node = self.head
            rtnVal = cur_node.value
            while cur_node != None:
                if cur_node.value >= rtnVal:
                    rtnVal = cur_node.value

                cur_node = cur_node.next_node

        return rtnVal

    def contains(self, target_val) -> bool:
        if self.head != None:
            cur_node = self.head
            while cur_node != None:
                if cur_node.value == target_val:
                    return True

                cur_node = cur_node.next_node

        return False

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.size += 1

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.size += 1

    def remove_head(self):
        return self._pop(True) if self.head != None else None

    def _pop(self, remove_head: bool):
        if remove_head:
            rtnVal = self.head.value
            self.head = self._delete(self.head.value, self.head)
        else:
            rtnVal = self.tail.value
            self.tail = self._delete(self.head.tail, self.tail)

        if self.head == None:
            self.tail = None

        return rtnVal

    def remove(self, target):
        self.head = self._delete(target, self.head)

    def _delete(self, target, cur_node) -> Node:
        if cur_node == None:
            return None

        if target == cur_node.value:
            next_node = cur_node.next_node
            self.size -= 1
            return next_node

        cur_node.next_node = self._delete(target, cur_node.next_node)
        if cur_node.next_node == None:
            self.tail = cur_node

        return cur_node
