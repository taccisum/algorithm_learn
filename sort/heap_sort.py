def left(index):
    return index * 2  + 1


def right(index):
    return index * 2 + 2


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def heapify(arr, index):
    l = left(index)
    r = right(index)

    largest = 0

    if l <= len(arr) - 1 and arr[l] > arr[index]:
        largest = l
    else:
        largest = index

    if r <= len(arr) - 1 and arr[r] > arr[largest]:
        largest = r

    if largest != index:
        swap(arr, index, largest)
        heapify(arr, largest)
    return arr


def non_leaf_index(length):
    return length / 2
    # return (length - 1) / 2 + 1


def build_max_heap(arr):
    i = non_leaf_index(len(arr))
    for j in range(i)[::-1]:
        heapify(arr, j)
    return arr


def extract_max(max_heap):
    m = max_heap[0]
    swap(max_heap, 0, len(max_heap) - 1)
    return m, heapify(max_heap[:-1], 0)


def heap_sort(arr):
    max_heap = build_max_heap(arr)
    sort_arr = []
    for i in range(len(max_heap)):
        m, new_heap = extract_max(max_heap)
        max_heap = new_heap
        sort_arr.append(m)
    return sort_arr


if __name__ == '__main__':
    # print(non_leaf_index(10))
    # print(heap_node([1,2,3], 0))   # 3,1,2
    # print(build_max_heap([1,2,3,4,5,6,7,8,9]))
    # print(extract_max(build_max_heap([1,2,3,4,5,6,7,8,9])))
    print '---heap sort---'
    print(heap_sort([1,2,3,4,5,6,7,8,9]))
    print(heap_sort([2,3,1,5,4,7,6,10,9]))