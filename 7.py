class Solution(object):
    def convert(self, s, numRows):
        if not numRows or numRows == 1 or len(s) <= numRows:
            return s

        dic = {}
        count = 0
        reverse = False
        for i in range(len(s)):
            if count < numRows and not reverse:
                if count in dic:
                    dic[count] += s[i]
                else:
                    dic[count] = s[i]
                count += 1
                if count == numRows:
                    reverse = True
            else:
                if count == numRows:
                    count -= 2
                else:
                    count -= 1
                dic[count] += s[i]
                if count == 0:
                    count += 1
                    reverse = False
        rtn = ""
        for i in range(numRows):
            rtn += dic[i]
        return rtn


# dic = {}
# s = "anmksced"
# dic[0] = s[1]
# dic[0] += s[2]
# print(dic)

class Solution2(object):
    def convert(self, s, numRows):
        if not numRows or numRows == 1 or len(s) <= numRows:
            return s
        dic = {}
        count = 0
        reverse = False
        for i in range(len(s)):
            if count < numRows and not reverse:
                if count in dic:
                    dic[count] += s[i]
                else:
                    dic[count] = s[i]
                count += 1
                if count == numRows:
                    reverse = True
            else:
                if count == numRows:
                    count -= 2
                else:
                    count -= 1
                dic[count] += s[i]
                if count == 0:
                    count += 1
                    reverse = False
        rtn = ""
        for i in range(numRows):
            rtn += dic[i]
        return rtn
