
# 1.两个for循环 去尝试每一种组合，如果和为目标值，即可返回， 时间复杂度 n2.
# 2.优化，空间换时间，使用字典存储遍历过得值和index， 如果目标值与当前值之差存在于字典中，说明存在某种组合满足目标值， 时间复杂度n。



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}        
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            else:
                dic[target - num] = i

                
