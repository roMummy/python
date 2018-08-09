import sys
import time


def dfs(nums, sums, index, tagert):
    """
    :param nums: List[int]
    :param sums: List[int]
    :param index: int
    :return: bool
    :tagert: int
    """
    if index == len(nums):
        #满足3个边都一样的就是正方形
        return sums[0] == sums[1] == sums[2]
    #递归 进行所有排列组合 满足条件就跳出递归
    for i in range(0, 3):
        #如果大于平均值就没有必要加入到子列表中
        if sums[i] + nums[index] > tagert:
            continue
        sums[i] += nums[index]
        if dfs(nums, sums, index + 1, tagert):
            return True
        sums[i] -= nums[index]
    return False


def makesquare(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    sum = 0
    sums = 4 * [0]
    for item in nums:
        sum += item
    #其它情况全部排除
    if n < 4 or sum % 4 != 0 or sum == 0 or n > 10:
        return False
    return dfs(nums, sums, 0, sum/4)

def times():
    start = time.clock()
    print(makesquare([1,1,2,2,2]))
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
times()

# print(makesquare([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]))



