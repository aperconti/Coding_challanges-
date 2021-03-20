hash = {}
target_num = 6
list_nums = [4,2,3,6,1,5,1]

def twosumhash(list_nums,target_num):
    for i in range(len(list_nums)-1):
        match = target_num - list_nums[i]
        if match in hash:
            print(f'Match found, Target Numer is: {target_num}, which is the same as {list_nums[i]} + {match}')

        hash[list_nums[i]] = list_nums[i]
twosumhash(list_nums,target_num)
