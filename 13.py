class Solution(object):
    def maxArea(self, height):
        right = len(height) - 1
        left = 0
        max_rol = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            col = w * h
            max_rol = max(col, max_rol)

            while height[left] <= h and left < right:left+=1
            while height[right] <= h and right > left:right-=1
            print(height[left], height[right])

        return max_rol

c = Solution()
height = [12, 1, 23, 11, 19, 9, 2]
c = c.maxArea(height)
print(c)

class Solution2(object):
    def maxArea(self, height):
        right = len(height) - 1
        left = 0
        max_rol = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            col = h * w
            max_rol = max(col, max_rol)

            while height[left] <= h and left < right:left+=1
            while height[right] <=h and right > left:right-=1

        return max_rol

c = Solution2()
height = [12, 1, 23, 11, 19, 9, 2]
c = c.maxArea(height)
print(c)
