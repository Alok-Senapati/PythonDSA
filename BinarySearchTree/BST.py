from BinaryTree.BinaryTree import Node, preorder


class BST:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def insert_node(self, data):
        if not self.__root:
            self.__root = Node(data)
        else:
            root = None
            node = self.__root
            while node:
                root = node
                if node.get_data() < data:
                    node = node.get_right()
                elif node.get_data() > data:
                    node = node.get_left()
                else:
                    return None
            if root.get_data() < data:
                root.set_right(data)
                return root
            elif root.get_data() > data:
                root.set_left(data)
                return root
            else:
                return None

    def search(self, data):
        root = self.__root
        while root:
            if root.get_data() == data:
                return True
            elif root.get_data() < data:
                root = root.get_right()
            else:
                root = root.get_left()
        return False


def min_value_node(root):
    while root and root.get_left():
        root = root.get_left()
    return root


def delete_node(root, data):
    if not root:
        return None

    if data < root.get_data():
        root.set_left_node(delete_node(root.get_left(), data))
    elif data > root.get_data():
        root.set_right_node(delete_node(root.get_right(), data))
    else:
        if (not root.get_left()) and (not root.get_right()):
            return None
        elif not root.get_left():
            return root.get_right()
        elif not root.get_right():
            return root.get_left()
        else:
            temp = min_value_node(root.get_right())
            root.set_data(temp.get_data())
            root.set_right_node(delete_node(root.get_right(), temp.get_data()))
    return root


def get_floor(root_node, data):
    floor = None
    while root_node:
        if root_node.get_data() > data:
            root_node = root_node.get_left()
        elif root_node.get_data() < data:
            floor = floor if floor and floor.get_data() > root_node.get_data() else root_node
            root_node = root_node.get_right()
        else:
            return root_node
    return floor


def get_ceil(root_node, data):
    ceil = None
    while root_node:
        if root_node.get_data() > data:
            ceil = ceil if ceil and ceil.get_data() < root_node.get_data() else root_node
            root_node = root_node.get_left()
        elif root_node.get_data() < data:
            root_node = root_node.get_right()
        else:
            return root_node
    return ceil


if __name__ == '__main__':
    bst = BST()
    bst.insert_node(4)
    bst.insert_node(3)
    bst.insert_node(2)
    bst.insert_node(9)
    bst.insert_node(1)
    bst.insert_node(5)
    preorder(bst.get_root())
    print()
    print(bst.search(8))
    # delete_node(bst.get_root(), 4)
    # preorder(bst.get_root())
    print(get_floor(bst.get_root(), 11))
    print(get_ceil(bst.get_root(), 2))
