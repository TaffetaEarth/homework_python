import matplotlib.pyplot as pt
import random
import time
from progress.spinner import Spinner


def sort_choice(nums):
    for i in range(len(nums)):
        lowest = i
        for k in range(i, len(nums)):
            if nums[k] < nums[lowest]:
                lowest = k
            nums[lowest], nums[i] = nums[i], nums[lowest]
    return nums


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums, e_nums, b_nums = [], [], []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                b_nums.append(n)
            else:
                e_nums.append(n)
    return quicksort(s_nums) + e_nums + quicksort(b_nums)


def bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


times1, ns, elements = [], [], []
times2, ns2 = [], []
times3, ns3 = [], []
state = ""
for n in range(100, 8100, 100):
    elements = [random.randrange(0, n) for _ in range(n)]
    elements1 = elements.copy()
    elements2 = elements1.copy()
    t = time.time()
    bubble(elements)
    work_time1 = time.time() - t
    times1.append(work_time1)
    t = time.time()
    quicksort(elements1)
    work_time2 = time.time() - t
    times2.append(work_time2)
    t = time.time()
    sort_choice(elements2)
    work_time3 = time.time() - t
    times3.append(work_time3)
    ns.append(n)
    print(n)
ax = pt.subplot()
ax2 = ax.twinx()
ax3 = ax2.twinx()
ax.plot(ns, times1, color='b')
ax2.plot(ns, times2, color='r')
ax3.plot(ns, times3, color='g')
pt.show()
