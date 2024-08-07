# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U']
        stack = []
        res = ''
        for i in range(0, len(s)):
            if s[i] in vowels:
                stack.append(s[i])
        
        res = ''

        for i in range(0, len(s)):
            if s[i] in vowels:
                res += stack.pop()
            else:
                res += s[i]
        
        return res
        