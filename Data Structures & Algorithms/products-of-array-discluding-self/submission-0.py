class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward, backward = [nums[0]]*n, [nums[-1]]*n
        for i in range(1, n):
            forward[i] = forward[i - 1] * nums[i]
            backward[(n-1)-i] = backward[(n-1)-(i-1)] * nums[(n-1)-i]
        return [backward[1]] + [
            forward[i-1] * backward[i+1]
            for i in range(1, n - 1)
            ] + [forward[n - 2]]