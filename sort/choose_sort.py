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

    # 时间复杂度最终可表示为O(n^2)

    return nums


if __name__ == '__main__':
    print(choose_sort([3, 1, 2, 5, 4]))
