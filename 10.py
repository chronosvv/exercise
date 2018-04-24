class Solution(object):
    def isMatch(self, s, p):
        sLen = len(s)
        pLen = len(p)
        if (pLen == 0):
            return sLen == 0
        if (pLen == 1):
            if (p == s) or ((p == '.') and (len(s) == 1)):
                return True
            else:
                return False

        if (p[-1] != '*') and (p[-1] != '.') and (p[-1] not in s):
            return False
        if (p[1] != '*'):
            if(len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                return self.isMatch(s[1:], p[1:])
            return False
        else:
            while(len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                if(self.isMatch(s, p[2:])):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

c = Solution()
a = c.isMatch("ccccca", "c*a")
print(a)

class Solution2(object):
    def isMatch(self, s, p):
        sLen = len(s)
        pLen = len(p)

        if (pLen == 0):
            return sLen == 0
        if (pLen == 1):
            if (p == s) or ((p == '.') and len(s) == 1):
                return True
            else:
                return False
        if (p[-1] != '*') and (p[-1] != '.') and (p[-1] not in s):
            return False
        if(p[1] != '*'):
            if(len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                return self.isMatch(s[1:], p[1:])
            return False
        else:
            while(len(s) > 0) and ((p[0] == s[0]) or (p[0] == '.')):
                if (self.isMatch(s, p[2:])):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])