class solution(object):
    def func(self, array, string, left, right):
        if left == 0 and right == 0:
            array += [string]
        if left > 0:
            self.func(array, string+"(", left-1, right)
        if right > 0 and left < right:
            self.func(array, string+")", left, right-1)

    def generateParenthese(self, n):
        rtn = []
        self.func(rtn, "", n, n)
        return rtn

class Solution2(object):
    def func(self, array, string, left, right):
        if left == 0 and right == 0:
            array += [string]
        if left > 0:
            self.func(array, string+"(", left-1, right)
        if right > 0 and left < right:
            self.func(array, string+")", left, right-1)

    def generateParenthese(self, n):
        rtn = []
        self.func(rtn, "", n, n)
        return rtn