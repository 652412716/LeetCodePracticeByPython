"""
两数之和：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。
但是，你不能重复利用这个数组中同样的元素。

实例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

链接：
https://leetcode-cn.com/problems/two-sum/
"""

# 测试用例
test_nums = [2, 7, 11, 15]
test_target = 9

# 解决方法


def two_nums_sum_1(nums, target):
    time = 0
    idx_list = [0, 0]
    for num in nums:
        num_2 = target - num
        if num_2 in nums:
            index_1 = time
            index_2 = nums.index(num_2)
            if index_1 != index_2:
                idx_list[0] = index_1
                idx_list[1] = index_2
                return idx_list

        time += 1

# 运行


print(two_nums_sum_1(test_nums, test_target))

#This is a test for git push
pass

