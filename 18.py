class Solution(object):
    def letterCombination(self, digits):
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
               "7":"pqrs", "8":"tuv", "9":"wxyz"}
        index = len(digits) - 1
        if index < 0:
            return []
        rtn = [""]

        while index > -1:
            rtn = [b+a for a in rtn for b in dic[digits[index]]]
            index -= 1

        return rtn

class Solution2(object):
    def letterCombination(self, digits):
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
               "7":"pqrs", "8":"tuv", "9":"wxyz"}
        index = len(digits) - 1
        if index < 0:
            return []
        rtn = [""]

        while index > -1:
            rtn = [b+a for a in rtn for b in dic[digits[index]]]
            index -= 1

        return rtn

