class Solution(object):
    def isValid(self, s):
        dic = {"(":")", "{":"}", "[":"]"}
        lis = []
        length = len(s)
        for i in range(length):
            if s[i] in dic:
                lis += [dic[s[i]]]
            else:
                if len(lis) < 1:
                    # print("<")
                    return False
                last = lis[-1]
                if last != s[i]:
                    return False
                else:
                    del lis[-1]

        if len(lis) == 0:
            return True
        else:
            return False
s = Solution()
strs = "]}"
s = s.isValid(strs)
print(s)

class Solution2(object):
    def isValid(self, s):
        dic = {"(":")", "{":"}", "[":"]"}
        lis = []
        length = len(s)
        for i in range(length):
            if s[i] in dic:
                lis += [dic[s[i]]]
            else:
                if len(lis) < 1:
                    return False
                last = lis[-1]
                if last != s[i]:
                    return False
                else:
                    del lis[-1]
        if len(lis) == 0:
            return True
        else:
            return False



