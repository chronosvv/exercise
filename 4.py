class Solution(object):
    def longest(self, s):
        if not s:
            return 0

        max_sub = ""
        find_sub = ""

        end = 0
        begin = 0

        while end < len(s):
            if find_sub.find(s[end]) < 0:
                find_sub += s[end]
                if end - begin + 1 > len(max_sub):
                    max_sub = s[begin:end+1]

            else:
                sub_begin = find_sub.find(s[end])

                begin += sub_begin+1
                find_sub = s[begin:end+1]

            end += 1

        return len(max_sub)

class Solution2(object):
    def longest(self, s):
        if not s:
            return 0

        max_sub = ""
        find_sub = ""

        begin = 0
        end = 0

        while end < len(s):
            if find_sub.find(s[end]) < 0:
                find_sub += s[end]
                if end - begin + 1 > len(max_sub):
                    max_sub = s[begin:end+1]

            else:
                sub_begin = find_sub.find(s[end])
                begin += sub_begin+1
                find_sub = s[begin:end+1]

            end += 1

        return len(max_sub)

s = "1234"
print(s[1:2])