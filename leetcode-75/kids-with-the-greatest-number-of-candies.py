# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxx = max(candies)
        for c in candies:
            result.append(c + extraCandies >= maxx)

        return result