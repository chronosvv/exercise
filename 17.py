class Solution(object):
    def threeSumClosest(self, nums, target):
        arr = sorted(nums)
        length = len(arr)
        final_sum = arr[0] + arr[1] + arr[2]
        final_gap = abs(final_sum - target)
        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = arr[start] + arr[i] + arr[end]
                this_gap = abs(value - target)

                if final_gap > this_gap:
                    final_sum = value
                    final_gap = this_gap
                if target > value:
                    start += 1
                else:
                    end -= 1
        return final_sum

s = Solution()
nums = [-1, 2, 1, -4]
s = s.threeSumClosest(nums, 1)
print(s)

class Solution2(object):
    def threeSumClosest(self, nums, target):
        arr = sorted(nums)
        length = len(arr)
        final_sum = arr[0] + arr[1] + arr[2]
        final_gap = abs(final_sum - target)

        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = arr[start] + arr[i] + arr[end]
                this_gap = abs(value - target)

                if final_gap > this_gap:
                    final_sum = value
                    final_gap = this_gap
                if target > value:
                    start += 1
                else:
                    end -= 1
        return final_sum