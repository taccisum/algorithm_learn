# 分治法


def find_max_crossing_sub_arr(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    sub_arr = arr[start:end+1]
    mid = int(len(sub_arr)/2)

    l_max_sum = None
    r_max_sum = None
    l_sum = 0
    r_sum = 0
    l_idx = None
    r_idx = None

    for i in range(0, mid)[::-1]:
        l_sum += sub_arr[i]
        if not l_max_sum or l_sum > l_max_sum:
            l_max_sum = l_sum
            l_idx = i

    for i in range(mid, len(sub_arr)):
        r_sum += sub_arr[i]
        if not r_max_sum or r_sum > r_max_sum:
            r_max_sum = r_sum
            r_idx = i

    return start + l_idx, start + r_idx, l_max_sum + r_max_sum


def find_max_sub_arr(arr, start, end):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1

    sub_arr = arr[start:end+1]

    if not sub_arr or len(sub_arr) == 0:
        return None
    elif len(sub_arr) == 1:
        return start, end, sub_arr[0]
    else:
        mid = int(len(sub_arr)/2)
        l_start, l_end, l_max_sum = find_max_sub_arr(arr, start, start + mid - 1)
        r_start, r_end, r_max_sum = find_max_sub_arr(arr, start + mid, end)
        c_start, c_end, c_max_sum = find_max_crossing_sub_arr(arr, start, end)

        if l_max_sum >= r_max_sum and l_max_sum >= c_max_sum:
            return l_start, l_end, l_max_sum
        elif r_max_sum >= l_max_sum and r_max_sum >= c_max_sum:
            return r_start, r_end, r_max_sum
        else:
            return c_start, c_end, c_max_sum

def find_max_sub_arr1(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr)-1

    sub_arr = arr[start:end+1]
    
    max_sum_before = sub_arr[start] 
    sum_before = sub_arr[start]

    for i in range(len(sub_arr)):
        sum_before += sub_arr[i]
        if sum_before < 0:
            sum_before = 0
            pass
        elif sum_before > max_sum_before:
            max_sum_before = sum_before

    if max_sum_before == 0:
        pass
    
    return max_sum_before


if __name__ == '__main__':
    print(find_max_crossing_sub_arr([1, 2, 3, -1, -2, -3]))    # 0, 3, 5
    print(find_max_crossing_sub_arr([-1, 2, -1, 3, 4, -2, -3]))     # 1, 4, 8
    print(find_max_crossing_sub_arr([2, 5, -1, 2, -6, 3, 4, 6, -2, -6, -4, 7]))     # 0, 7, 15
    print('#####')
    print(find_max_sub_arr([4, 5, 6, -1, -2, -3, 7, 8, 9, -1], 0, 9))   # 0, 8, 33
    print(find_max_sub_arr1([-1, 4, 5, 6, -1, -2, -3, 7, 8, 9, -1], 0, 10))
    print(find_max_sub_arr1([-1,1,2,-10,10]))
    print(find_max_sub_arr1([-1,1,2,-10]))
