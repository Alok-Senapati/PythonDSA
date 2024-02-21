from queue import SimpleQueue


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

    def get_right(self):
        return self.__right

    def set_left(self, data):
        new_node = Node(data)
        self.__left = new_node

    def set_right(self, data):
        new_node = Node(data)
        self.__right = new_node

    def set_left_node(self, data_node):
        self.__left = data_node

    def set_right_node(self, data_node):
        self.__right = data_node

    def __str__(self):
        return str(self.__data)


def preorder(root_node):
    print(root_node.get_data(), end=" ")
    if ln := root_node.get_left():
        preorder(ln)
    if root_node.get_right():
        preorder(root_node.get_right())


def inorder(root_node):
    if root_node.get_left():
        inorder(root_node.get_left())
    print(root_node.get_data(), end=" ")
    if root_node.get_right():
        inorder(root_node.get_right())


def postorder(root_node):
    if root_node.get_left():
        postorder(root_node.get_left())
    if root_node.get_right():
        postorder(root_node.get_right())
    print(root_node.get_data(), end=" ")


def height(root_node):
    if root_node is None:
        return 0
    return 1 + max(height(root_node.get_left()), height(root_node.get_right()))


def print_at_k(root_node, k):
    if k == 0:
        print(root_node.get_data(), end=" ")
        return
    print_at_k(root_node.get_left(), k-1)
    print_at_k(root_node.get_right(), k-1)


def level_order(root_node):
    q = SimpleQueue()
    q.put(root_node)
    while not q.empty():
        c = q.qsize()
        for i in range(c):
            node = q.get()
            print(node.get_data(), end=" ")
            if node.get_left():
                q.put(node.get_left())
            if node.get_right():
                q.put(node.get_right())
        print()


def tree_to_dll(root_node):
    global prev
    if root_node is None:
        return root_node
    head = tree_to_dll(root_node.get_left())
    if prev is None:
        head = root_node
    else:
        root_node.set_left_node(prev)
        prev.set_right_node(root_node)
    prev = root_node
    tree_to_dll((root_node.get_right()))
    return head


def print_dll(head_node):
    while head_node is not None:
        print(head_node.get_data(), end=" ")
        head_node = head_node.get_right()
    print()


def tree_in_pre(_in, _pre, in_start, in_end):
    global pre_index
    if in_start > in_end:
        return None
    new_node = Node(_pre[pre_index])
    pre_index += 1
    # if in_start == in_end:
    #     return new_node
    in_index = 0
    for i in range(in_start, in_end + 1):
        if _in[i] == new_node.get_data():
            in_index = i
            break

    new_node.set_left_node(tree_in_pre(_in, _pre, in_start, in_index - 1))
    new_node.set_right_node(tree_in_pre(_in, _pre, in_index + 1, in_end))
    return new_node


def tree_in_post(_in, _post, in_start, in_end):
    global post_index
    if in_start > in_end:
        return None
    new_node = Node(_post[post_index])
    post_index -= 1

    in_index = 0
    for i in range(in_start, in_end + 1):
        if _in[i] == new_node.get_data():
            in_index = i
            break

    new_node.set_right_node(tree_in_post(_in, _post, in_index+1, in_end))
    new_node.set_left_node(tree_in_post(_in, _post, in_start, in_index-1))
    return new_node


if __name__ == '__main__':
    root = Node(1)
    root.set_left(2)
    root.set_right(3)
    root.get_left().set_left(4)
    root.get_left().set_right(5)
    root.get_right().set_left(6)
    root.get_right().set_right(7)
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    print()
    print("Height of the tree is:", height(root))
    print_at_k(root, 2)
    print()
    level_order(root)
    prev = None
    head_dll = tree_to_dll(root)
    print_dll(head_dll)
    pre_index = 0
    new_root = tree_in_pre([4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7], 0, 6)
    print()
    postorder(new_root)
    post_index = 6
    new_root = tree_in_post([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1], 0, 6)
    print()
    preorder(new_root)
