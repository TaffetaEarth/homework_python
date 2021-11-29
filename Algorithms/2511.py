def sort_choice(nums):
    for i in range(len(nums)):
        lowest = i
        for k in range(i, len(nums)):
            if nums[k] < nums[lowest]:
                lowest = k
            nums[lowest], nums[i] = nums[i], nums[lowest]
    return nums


def dia_sort(nums):
    acc = []
    for i in range(min(len(nums), len(nums[1]))):
        acc.append(nums[i][i])
    acc = sort_choice(acc)
    for k in range(len(acc)):
        nums[k][k] = acc[k]
    return nums


print(dia_sort(
    [[1, 2, 3],
     [3, 3, 1],
     [1, 2, 2]]
))


def sort_choice_letters(stroka):
    nums = []
    for k in range(len(stroka)):
        nums.append(stroka[k])
    for l in nums:
        if l.isdigit() or l.isalpha():
            continue
        else:
            return "Err"
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if ord(nums[i]) > ord(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    return "".join(nums)


print(sort_choice_letters("abd45c"))


def stpd(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i][1] < list[j][1]:
                list[i], list[j] = list[j], list[i]
            if list[i][1] == list[j][1]:
                if list[i][2] < list[j][2]:
                    list[i], list[j] = list[j], list[i]
                if list[i][2] == list[j][2]:
                    k = 0
                    while ord(list[i][0][k]) == ord(list[j][0][k]):
                        if k < min(len(list[i][0]), len(list[j][0])) - 1:
                            k += 1
                        else:
                            break
                    if list[i][0][k] > list[j][0][k]:
                        list[i], list[j] = list[j], list[i]
    return list


a = [("Иванов", 4.3, 183), ("Петров", 4.7, 169), ("Иванов", 4.3, 200), ("Ванов", 4.3, 200)]
print(stpd(a))
