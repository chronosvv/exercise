class Solution:
    def intToRoman(self, num):
        s = ''
        if num / 1000 != 0:
            s = self.RomanDigit(s, num//1000, 'M', '#', '#')
            num %= 1000
        if num / 100 != 0:
            s = self.RomanDigit(s, num//100, 'C', 'D', 'M')
            num %= 100
        if num / 10 != 0:
            s = self.RomanDigit(s, num//10, 'X', 'L', 'C')
            num %= 10
        if num != 0:
            s = self.RomanDigit(s, num, 'I', 'V', 'X')
        return s

    def RomanDigit(self, s, digit, a, b, c):
        if digit < 4:
            s += a * digit
            return s
        elif digit == 4:
            s += a + b
            return s
        elif digit < 9:
            s += b + a * (digit - 5)
            return s
        else:
            s += a + c
            return s

c = Solution()
a = c.intToRoman(1948)
print(a)