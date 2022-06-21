#!/usr/bin/python3
'''Node and Singly linked list module'''


class Node:
    '''Represents node of a singly linked list.
    Attributes:
      data (int): Data to store in node.
      next_node (node): Next node (default=None).'''

    def __init__(self, data, next_node=None):
        '''Initialize data.
        Args:
          data (int): Data to store
          next_node (node): next node.'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Data accessor.
        Returns:
          data.'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Data mutator.
        Args:
          value (int): Data to use.'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''next_node accessor.
        Returns:
          next_node.'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''next_node mutator.
        Args:
          value (node): next node'''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Represents a singly linked list.
    Attributes:
      head: Head of list.
     Methods:
      sorted_instance: Inserts new node into a given index of sorted list.'''

    def __init__(self):
        '''Initialize linked list.'''
        self.head = None

    def __str__(self):
        '''For the print statement in the main file.'''
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        '''Inserts a node in a sorted linked list.
        Args:
          value (int): new data to store.'''
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = 
