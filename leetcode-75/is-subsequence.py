# https://leetcode.com/problems/is-subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        for j in range(len(t)):
            if i >= len(s):
                return True
            if t[j] == s[i]:
                i += 1
        return i >= len(s)