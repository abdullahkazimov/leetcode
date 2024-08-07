# https://leetcode.com/problems/reverse-words-in-a-string

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = ' '.join(list(reversed(s.strip().split())))
        return s