from BinaryTree import Node
from queue import SimpleQueue


def preorder(root):
    print(root.get_data(), end=" ")
    if nl := root.get_left():
        preorder(nl)
    if nr := root.get_right():
        preorder(nr)


def inorder(root):
    if nl := root.get_left():
        inorder(nl)
    print(root.get_data(), end=" ")
    if nr := root.get_right():
        inorder(nr)


def postorder(root):
    if nl := root.get_left():
        postorder(nl)
    if nr := root.get_right():
        postorder(nr)
    print(root.get_data(), end=" ")


def levelorder(root):
    q = SimpleQueue()
    q.put(root)
    q.put(None)
    while q.qsize() > 1:
        node = q.get()
        if node is None:
            q.put(None)
            print()
            continue
        print(node.get_data(), end=" ")
        if nl := node.get_left():
            q.put(nl)
        if nr := node.get_right():
            q.put(nr)


def spiral(root, reverse=True):
    if not root:
        return None
    q = SimpleQueue()
    s = []
    q.put(root)
    s.append(root)
    while not q.empty():
        c = q.qsize()
        for i in range(c):
            node = q.get()
            if reverse:
                print(s.pop().get_data(), end=" ")
            else:
                print(node.get_data(), end=" ")
                if nl := node.get_left():
                    s.append(nl)
                if nr := node.get_right():
                    s.append(nr)
            if nl := node.get_left():
                q.put(nl)
            if nr := node.get_right():
                q.put(nr)
        reverse = not reverse
        print()


max_level = 0


def print_left_recursive(root, level):
    global max_level
    if not root:
        return
    if level > max_level:
        print(root.get_data(), end=" ")
        max_level = level
    print_left_recursive(root.get_left(), level + 1)
    print_left_recursive(root.get_right(), level + 1)


def print_left_iterative(root):
    q = SimpleQueue()
    q.put(root)
    while not q.empty():
        s = q.qsize()
        for i in range(s):
            node = q.get()
            if i == 0:
                print(node.get_data(), end=" ")
            if nl := node.get_left():
                q.put(nl)
            if nr := node.get_right():
                q.put(nr)


def print_leftview(root):
    print("Left view of the tree using Recursion :", end=" ")
    print_left_recursive(root, 1)
    print()
    print("Left view of the tree using Iteration :", end=" ")
    print_left_iterative(root)


def size(root):
    if not root:
        return 0
    return size(root.get_left()) + size(root.get_right()) + 1


def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.get_left()), get_height(root.get_right()))


def get_dia(root):
    if not root:
        return 0, 0
    hl, dl = get_dia(root.get_left())
    hr, dr = get_dia(root.get_right())
    height = max(hl, hr) + 1
    dia = max(hl + hr + 1, dl, dr)
    return height, dia


def max_tree(root):
    if not root:
        return float("-inf")
    return max(max_tree(root.get_left()), max_tree(root.get_right()), root.get_data())


def is_children_sum(root):
    if not root:
        return True
    if root.get_left() is None and root.get_right() is None:
        return True
    curr_val = 0
    if nl := root.get_left():
        curr_val += nl.get_data()
    if nr := root.get_right():
        curr_val += nr.get_data()
    return (root.get_data() == curr_val) and is_children_sum(root.get_left()) and is_children_sum(root.get_right())


# A binary tree is called to be hide balanced if The difference between height of its left subtree
# and height of its right subtree it's not more than one recursively.
def is_height_balanced(root):
    if not root:
        return 0, True
    hl, bl = is_height_balanced(root.get_left())
    hr, br = is_height_balanced(root.get_right())
    balanced = abs(hl - hr) <= 1 and bl and br
    height = 1 + max(hl, hr)
    return height, balanced


def max_width(root):
    if not root:
        return 0
    q = SimpleQueue()
    q.put(root)
    mw = 0
    while not q.empty():
        c = q.qsize()
        mw = max(mw, c)
        for i in range(c):
            node = q.get()
            if nl := node.get_left():
                q.put(nl)
            if nr := node.get_right():
                q.put(nr)
    return mw


def klevel_node(root, k):
    if not root:
        return
    elif k == 0:
        print(root.get_data(), end=" ")
    else:
        klevel_node(root.get_left(), k - 1)
        klevel_node(root.get_right(), k - 1)


prev = None


def tree_to_dll(root):
    global prev
    if not root:
        return root
    head = tree_to_dll(root.get_left())
    if not prev:
        head = root
    else:
        prev.set_right_node(root)
        root.set_left_node(prev)
    prev = root
    tree_to_dll(root.get_right())
    return head


def traverse_dll(head):
    root = head
    while root:
        print(root.get_data(), end=" ")
        root = root.get_right()
    print()


def main():
    root = Node(1)
    root.set_left(2)
    root.set_right(3)
    root.get_left().set_left(4)
    root.get_left().set_right(5)
    root.get_right().set_left(6)
    root.get_right().set_right(7)
    root.get_right().get_right().set_left(8)
    root.get_right().get_right().get_left().set_right(9)
    print("Preorder :", end=" ")
    preorder(root)
    print()
    print("Inorder :", end=" ")
    inorder(root)
    print()
    print("Postorder :", end=" ")
    postorder(root)
    print()
    print("Levelorder :")
    levelorder(root)
    print()
    h = get_height(root)
    n = size(root)
    m = max_tree(root)
    print(f"Size of the tree is : {n}")
    print(f"Height of the tree is : {get_height(root)}")
    print(f"Maximum node of the tree is : {m}")
    for k in range(h):
        print(f"Nodes at level {k} :")
        klevel_node(root, k)
        print()
    print_leftview(root)
    print()
    print("Is height balanced ?", end=" ")
    height, balanced = is_height_balanced(root)
    if balanced:
        print("Yes")
    else:
        print("No")
    print(f"Height of the tree is {height}")
    print(f"Max-width of the tree is {max_width(root)}")
    print("Spiral Traversal : ")
    spiral(root)
    print()
    print("Tree to DLL", end=" : ")
    traverse_dll(tree_to_dll(root))



if __name__ == '__main__':
    main()
