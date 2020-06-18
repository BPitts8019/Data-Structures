"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   The difference was minimal as the Linked list was designed to act very 
   similar to a list. However, the implementation of the Linked List too
   several iterations to get correct.
"""

from linked_list import LinkedList
# Stack implemented with a Custom Linked List


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = len(self.storage)

    def pop(self):
        rtnVal = None

        if (self.size > 0):
            rtnVal = self.storage.remove_head()
            self.size = len(self.storage)

        return rtnVal

# Stack implemented with a Python list
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.insert(0, value)
#         self.size = len(self.storage)

#     def pop(self):
#         rtnVal = None

#         if (self.size > 0):
#             rtnVal = self.storage.pop(0)
#             self.size = len(self.storage)

#         return rtnVal
