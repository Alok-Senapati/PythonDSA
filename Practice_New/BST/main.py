from BinaryTree import Node
from BinaryTree import inorder, preorder


class BST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, data):
        if not self.__root:
            self.__root = Node(data)
        else:
            curr = self.__root
            while curr:
                if(cd := curr.get_data()) == data:
                    return
                elif cd > data:
                    if not (cl := curr.get_left()):
                        curr.set_left(data)
                        break
                    else:
                        curr = cl
                else:
                    if not (cr := curr.get_right()):
                        curr.set_right(data)
                        break
                    else:
                        curr = cr

    def search(self, data):
        if self.__root:
            curr = self.__root
            while curr:
                if (cd := curr.get_data()) == data:
                    return True
                elif cd > data:
                    curr = curr.get_left()
                else:
                    curr = curr.get_right()
            else:
                return False
        return False

    def __in_successor(self, node):
        node = node.get_right()
        while node and (nl := node.get_left()):
            node = nl
        return node

    def delete(self, data, root=Node(None)):
        if not root:
            return None
        if root.get_data() is None:
            root = self.__root
        if (cd := root.get_data()) == data:
            if root.get_left() and root.get_right():
                ins = self.__in_successor(root)
                root.set_right_node(self.delete(ins.get_data(), root.get_right()))
                root.set_data(ins.get_data())
            elif rl := root.get_left():
                return rl
            elif rr := root.get_right():
                return rr
            else:
                return None
        elif cd > data:
            root.set_left_node(self.delete(data, root.get_left()))
        else:
            root.set_right_node(self.delete(data, root.get_right()))
        return root


def main():
    bst = BST()
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    print("Inorder", end=" : ")
    inorder(bst.root)
    print()
    print("Preorder", end=" : ")
    preorder(bst.root)
    print()
    print(bst.search(-1))
    print("Delete")
    bst.delete(-1)
    print("Inorder", end=" : ")
    inorder(bst.root)
    print()
    print("Preorder", end=" : ")
    preorder(bst.root)
    print()


if __name__ == '__main__':
    main()
