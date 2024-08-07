# https://leetcode.com/problems/can-place-flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt_odd = 0
        cnt_even = 0
        m = len(flowerbed)

        if m == 1:
            if flowerbed[0] == 0:
                return 1>=n
            
            return 0>=n

        i = 0
        while i < m:
            if flowerbed[i] == 0:
                if i == 0:
                    if i + 1 < m and flowerbed[i+1] == 0:
                        cnt_odd += 1
                elif i == m-1:
                    if i - 1 >= 0 and flowerbed[i-1] == 0:
                        cnt_odd += 1
                else:
                    if flowerbed[i-1] == flowerbed[i+1] == 0:
                        cnt_odd += 1
            i += 2
        
        i = 1
        while i < m:
            if flowerbed[i] == 0:
                if i == m-1:
                    if i - 1 >= 0 and flowerbed[i-1] == 0:
                        cnt_even += 1
                else:
                    if flowerbed[i-1] == flowerbed[i+1] == 0:
                        cnt_even += 1
            i += 2
        
        # print(cnt_odd)
        # print(cnt_even)
        return max(cnt_odd, cnt_even) >= n