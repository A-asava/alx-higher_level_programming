#!/usr/bin/python3
"""Define a class"""


class Node:
    """Represents a class node"""

    def __init__(self, data, next_node=None):
        """Initialize a class node
        Args:
            data: data to be inserted in the node
            next_node: next node of the list
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data in the class"""

        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked class"""

    def __init__(self):
        """Initialization of the class"""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the list
        Args:
            value: data to be inserted in the list
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while(temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Represents the print of a singly linked list"""

        value = []
        temp = self.__head
        while(temp is not None):
            value.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(value))
