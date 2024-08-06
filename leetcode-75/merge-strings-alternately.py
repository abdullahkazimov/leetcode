# T.C. = O(n+m) where n=len(word1) and m=len(word2)
# https://leetcode.com/problems/merge-strings-alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        
        ans = ''

        n,m = min(n,m), max(n,m)

        for i in range(2*n):
            if i % 2 == 0:
                ans += word1[i//2]
            else:
                ans += word2[(i-1)//2]
                
        if m == len(word1):
            ans += word1[n:]
        else:
            ans += word2[n:]

        return ans
