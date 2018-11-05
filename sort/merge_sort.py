import sys


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


if __name__ == '__main__':
    print(merge_sort([3, 1, 2, 5, 4]))
