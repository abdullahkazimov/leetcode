# https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        bests = []
        i = 0
        j = len(height) - 1
        while i < j:
            curr = (j-i) * min(height[i], height[j])
            bests.append(curr)
            left = height[i]
            right = height[j]
            if left > right:
                j -= 1
            else:
                i += 1
        return max(bests)