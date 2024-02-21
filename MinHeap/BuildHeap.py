def get_parent(heap, s):
    if s <= 0 or s >= len(heap):
        return None
    return s - 1 // 2


def get_left_child(heap, s):
    if s < 0 or s >= len(heap) or s * 2 + 1 >= len(heap):
        return None
    return s * 2 + 1


def get_right_child(heap, s):
    if s < 0 or s >= len(heap) or s * 2 + 2 >= len(heap):
        return None
    return s * 2 + 2


def min_heapify(heap, s):
    smallest = s

    left = get_left_child(heap, s)
    right = get_right_child(heap, s)
    if left is not None and heap[left] < heap[smallest]:
        smallest = left
    if right is not None and heap[right] < heap[smallest]:
        smallest = right

    if smallest != s:
        heap[s], heap[smallest] = heap[smallest], heap[s]
        min_heapify(heap, smallest)


def build_heap(heap):
    for i in range(len(heap) - 1 // 2, -1, -1):
        min_heapify(heap, i)
    return heap


if __name__ == '__main__':
    heap_list = build_heap([4, 6, 5, 1, 3, 7, 0, 9, 2, 11])
    print(' '.join(map(str, heap_list)))
