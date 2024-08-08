# https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = None
        zero_cnt = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                if not prod:
                    prod = nums[i]
                else:
                    prod *= nums[i]
            else:
                zero_cnt += 1
        
        if zero_cnt == len(nums):
            prod = 0

        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_cnt == 1:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                if zero_cnt == 0:
                    res.append(prod/nums[i])
                else:
                    res.append(0)
                
        return res