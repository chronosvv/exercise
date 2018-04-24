class Solution(object):
    def __init__(self):
        self.unique = []

    def threeSum(self, nums, target, v):
        length = len(nums)
        if length < 3:
            return None
        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = nums[i] + nums[start] + nums[end]
                if value == target and [v,nums[i],nums[start],nums[end]] not in self.unique:
                    self.unique += [[v,nums[i], nums[start],nums[end]]]
                    start += 1
                    end -= 1
                elif value < target:
                    start += 1
                else:
                    end -= 1

    def fourSum(self, nums, target):
        arr = sorted(nums)
        length = len(arr)
        for i in range(length):
            self.threeSum(arr[i+1:], target-arr[i], arr[i])

        return self.unique

class Solution2(object):
    def __init__(self):
        self.unique = []

    def threeSum(self, nums, target, v):
        length = len(nums)
        if length < 3:
            return None
        for i in range(length):
            start = i + 1
            end = length - 1
            while start < end:
                value = nums[i] + nums[start] + nums[end]
                if value==target and [v,nums[i],nums[start],nums[end]] not in self.unique:
                    self.unique += [[v, nums[i], nums[start], nums[end]]]
                    start += 1
                    end -= 1

                elif value < target:
                    start += 1

                else:
                    end -= 1
    def fourSum(self, nums, target):
        arr = sorted(nums)
        length = len(arr)
        for i in range(length):
            self.threeSum(arr[i+1:], target-arr[i], arr[i])

        return self.unique


