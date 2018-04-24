class Solution(object):
    def threeSum(self, nums):
        arr = sorted(nums)
        length = len(arr)
        hash_data = {}
        rtn = []
        last = None
        for i in range(length - 2):
            if last == arr[i]:
                continue
            last = arr[i]
            start = i + 1
            end = length - 1
            value = arr[i]
            while start < end:
                total = arr[start] + arr[end] + value
                if total == 0:
                    key = str(arr[start]) + ":" + str(arr[end])
                    if key not in hash_data:
                        rtn += [[value, arr[start], arr[end]]]
                        hash_data[key] = 0
                    else:
                        end -= 1
                        start += 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

        return rtn

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
s = s.threeSum(nums)
print(s)

class Solution2(object):
    def threeSum(self, nums):
        arr = sorted(nums)
        length = len(arr)
        hash_data = {}
        rtn = []
        last = None
        for i in range(length - 2):
            if last == arr[i]:
                continue
            last = arr[i]
            start = i + 1
            end = length - 1
            value = arr[i]
            while start < end:
                total = arr[start] + value + arr[end]
                if total == 0:
                    key = str(arr[start]) + ":" + str(arr[end])
                    if key not in hash_data:
                        rtn += [[value, arr[start], arr[end]]]
                        hash_data[key] = 0
                    else:
                        end -= 1
                        start += 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return rtn
    