class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


def search(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    for node in root.children:
        if search(node, data):
            return True
    return False


def isSamePath(root, node1, node2):
    if root.data == node1:
        if search(root, node2):
            return True
    elif root.data == node2:
        if search(root, node1):
            return True
    else:
        for child in root.children:
            flag1 = search(child, node1)
            flag2 = search(child, node2)
            if flag1 and flag2:
                return True
        return False
    return False


def main():
    root = Node(1)
    root.children = [Node(2), Node(3)]
    root.children[0].children = [Node(4), Node(5)]
    root.children[1].children = [Node(6)]
    root.children[0].children[1].children = [Node(7), Node(8), Node(9)]
    print("Result :", isSamePath(root, 4, 3))


if __name__ == '__main__':
    main()