import sys

def insert_sort(nums, asc):
    new_nums = [nums[0]]
    for i in range(1, len(nums)):
        index = 0
        if asc:
            for j in range(len(new_nums)):
                if new_nums[j] < nums[i]:
                    index = j + 1
                else:
                    break
        else:
            for j in range(len(new_nums)):
                if new_nums[j] > nums[i]:
                    index = j + 1
                else:
                    break

        new_nums.insert(index, nums[i])
    return new_nums


def choose_sort(nums):
    def find_min_index(nums):
        index = 0
        min = nums[index]
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
                index = i
        return index

    def swap(nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

    for i in range(1, len(nums)):   # c1 * n
        right = nums[i-1:len(nums)]     # c2 * (n-1)
        min_index = find_min_index(right)   # c3 * (n-1) * 求和tl(l=n->1)
        swap(nums, i-1, min_index + i - 1)  # c4 * (n-1)

    # 时间复杂度最终可表示为O(n2)

    return nums


def merge(sorted_nums_a, sorted_nums_b):
    # 时间复杂度O(n)
    def get(ls, idx, default=None):
        try:
            return ls[idx]
        except IndexError:
            return default

    merged_sorted_nums = []

    a_idx = 0
    b_idx = 0
    for i in range(len(sorted_nums_a) + len(sorted_nums_b)):
        min = None
        a_top = get(sorted_nums_a, a_idx, sys.maxsize)
        b_top = get(sorted_nums_b, b_idx, sys.maxsize)

        if a_top < b_top:
            min = a_top
            a_idx += 1
        elif a_top >= b_top:
            min = b_top
            b_idx += 1
        else:
            continue
        merged_sorted_nums.append(min)
    return merged_sorted_nums

def merge_sort(nums):
    # 时间复杂度O(n*lgn)
    if len(nums) <= 1:
        return nums
    mid = int(len(nums)/2)
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def bin_find(nums, num):
    if len(nums) <= 0:
        print('not found')
        return None
    mid = int(len(nums)/2)
    if nums[mid] > num:
        print('search %s' % nums[:mid])
        return bin_find(nums[:mid], num)
    elif nums[mid] < num:
        print('search %s' % nums[mid + 1:])
        return bin_find(nums[mid + 1:], num)
    elif nums[mid] == num:
        print('found')
        return nums[mid]


if __name__ == '__main__':
    print(insert_sort([3, 1, 4, 2, 5], False))
    print(insert_sort([3, 1, 4, 2, 5], True))
    print(choose_sort([3, 1, 2, 5, 4]))
    print(merge_sort([3, 1, 2, 5, 4]))
    print(bin_find(merge_sort([3, 1, 2, 5, 4]), 3))
    print(bin_find(merge_sort([3, 1, 2, 5, 4]), 4))
    print(bin_find(merge_sort([3, 1, 2, 5, 4]), 5))
    print(bin_find(merge_sort([3, 1, 2, 5, 4]), 6))
    print(bin_find(merge_sort([3, 1, 2, 5, 4]), 0))
