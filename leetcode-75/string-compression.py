# https://leetcode.com/problems/string-compression

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def _split(n):
            assert type(n) == str, 'it should be string'
            x = []
            for i in n:
                x.append(i)
            return x
        arr = []
        i=0
        cnt=None
        while i < len(chars):
            if i == 0:
                cnt = 1
            else:
                if chars[i] == chars[i-1]:
                    cnt += 1
                else:
                    arr.append(str(chars[i-1]))
                    if cnt > 1:
                        arr+=_split(str(cnt))
                        cnt = 1
            i+=1
                
        arr.append(str(chars[i-1]))
        if cnt > 1:
            arr+=_split(str(cnt))
            cnt = 1

        # print(arr)
        for i in range(len(arr)):
            chars[i] = arr[i]
        return len(arr)