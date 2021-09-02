from typing import List


def two_sum_old(nums: List[int], target: int) -> List[int]:
    check_num = 0
    for j in range(len(nums)):
        for i in range(len(nums)):
            if i == check_num:
                continue
            check_sum = nums[check_num] + nums[i]
            if check_sum == target:
                result = [check_num, i]
                return result
        check_num += 1


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_indeces = range(len(nums))
    check_dict = dict(zip(nums, list(nums_indeces)))
    for i in nums_indeces:
        check_num = target - nums[i]
        if check_num in check_dict:
            b = check_dict.get(check_num)
            if i == b:
                continue
            return [i, b]


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums=nums, target=target)
print('1st test: ', result)

nums = [3, 2, 4]
target = 6
result = two_sum(nums=nums, target=target)
print('2st test: ', result)

nums = [3, 3]
target = 6
result = two_sum(nums=nums, target=target)
print('3st test: ', result)
