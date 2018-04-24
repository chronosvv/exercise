class Solution(object):
    def __init__(self):
        self.low = 0
        self.R = 0

    def longest(self, s):
        if s == None or len(s) == 1:
            return s
        for i in range(len(s)):
            self.judge(s, i, i)
            self.judge(s, i, i+1)
        return s[self.low : self.low+self.R]

    def judge(self, string, start, end):
        while 0<start and end<len(string) and string[start] == string[end]:
            if end - start + 1 > self.R:
                self.R = end -start + 1
                self.low = start
            start -= 1
            end += 1

class Solution2(object):
    def __init__(self):
        self.low = 0
        self.R = 0

    def longest(self, s):
        if s == None or len(s) == 1:
            return s
        for i in range(len(s)):
            self.judge(s, i, i)
            self.judge(s, i, i+1)
        return s[self.low : self.low+self.R]

    def judge(self, string, start, end):
        while 0<start and end<len(string) and string[start] == string[end]:
            if end - start + 1 > self.R:
                self.R = end - start + 1
                self.low = start
            start -= 1
            end += 1