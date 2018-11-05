def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def split(arr, start, end):
    if end < start:
        end = start
    i = start - 1
    mid = arr[end]
    for j in range(start, end):
        if arr[j] <= mid:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, end)
    return arr, i + 1


def fast_sort(arr, start, end):
    if end - start > 1:
        arr, mid = split(arr, start, end)
        fast_sort(arr, start, mid - 1)
        fast_sort(arr, mid + 1, end)
    return arr


if __name__ == '__main__':
    # print(swap([1,2,3], 0, 2))
    # print(split([2,5,3,4,1,6,3,7,4], 0, 8))
    # print(split([2], 0, 0))
    # print(split([2,1], 0, 1))
    # print(split([2,1], 0, -1))

    print(fast_sort([2, 5, 9, 3, 7, 1], 0, 5))
