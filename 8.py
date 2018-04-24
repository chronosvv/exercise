class Solution(object):
    def reverse(self, x):
        y = 0
        flag = True
        if x < 0:
            flag = False
            x = abs(x)

        max_v = 2 ** 31 -1
        max_neg_v = 2 ** 31

        while x != 0:
            y = y * 10 + x % 10
            x = int(x / 10)

            if flag and y > max_v:
                return 0
            elif not flag and y > max_neg_v:
                return 0

        if flag:
            return y
        else:
            return -y

class Solution2(object):
    def reverse(self, x):
        y = 0
        flag = True
        if x < 0:
            flag = False
            x = abs(x)

        max_v = 2 ** 31 -1
        max_neg_v = 2 ** 31
        while x != 0:
            y = y * 10 + x % 10
            x = int(x / 10)

            if flag and y > max_v:
                return 0
            elif not flag and y > max_neg_v:
                return 0

        if flag:
            return y
        else:
            return -y