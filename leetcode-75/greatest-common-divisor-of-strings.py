# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)

        def gcd(a,b):
            if b == 0:
                return a
            
            return gcd(b, a%b)

        g = gcd(n, m)
        ans = str1[:g]

        if not  (ans * (n/g) == str1 and ans * (m/g) == str2):
            ans = ''

        return ans