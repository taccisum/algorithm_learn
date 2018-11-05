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


if __name__ == '__main__':
    print(insert_sort([3, 1, 4, 2, 5], False))
    print(insert_sort([3, 1, 4, 2, 5], True))
