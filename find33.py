def has_33(nums):
    # i = 0
    # if i <= len(nums):
        for i in range(0, len(nums) - 1):
            print(i,nums[i])
            if nums[i] == nums[i+1]:
                return True
        return False


#     i = 0
#     for item in nums:
#         print (nums[i])
#         if nums[i] == nums[i+1]:
#             return True
#         # if nums[item] == nums[item+1]:
#         #     return True
#         # else:
#         #     return False
#         i += 1
nums = [1, 3, 3]
# # my_list1 = [1, 3, 1, 3]
# # my_list2 = [3, 1, 3]
has_33(nums)