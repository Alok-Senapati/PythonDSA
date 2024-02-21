# Implementation of Binary Tree

class Node:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_left(self):
        return self.__left

    def set_left(self, data):
        self.__left = Node(data)

    def get_right(self):
        return self.__right

    def set_right(self, data):
        self.__right = Node(data)

    def set_left_node(self, node):
        self.__left = node

    def set_right_node(self, node):
        self.__right = node

