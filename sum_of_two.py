list_of_nums = [8, 2, 4, 7, 5, 3]

target_sum = 9


def match_number(list_of_nums, target_sum):
    for i in range(len(list_of_nums) - 1):
        for j in range(i + 1, len(list_of_nums)):
            if list_of_nums[i] + list_of_nums[j] == target_sum:
                print(
                    f' The two numbers that equal the target sum are {list_of_nums[i]} + {list_of_nums[j]}')


match_number(list_of_nums, target_sum)
