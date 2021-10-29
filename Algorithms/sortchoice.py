def sort_choice(nums):
    for i in range(len(nums)):
        lowest = i
        for k in range(i, len(nums)):
            if nums[k] < nums[lowest]:
                lowest = k
            nums[lowest], nums[i] = nums[i], nums[lowest]
    return nums


print(sort_choice([1, 2, 3, 0, 3, 7, 0]))
