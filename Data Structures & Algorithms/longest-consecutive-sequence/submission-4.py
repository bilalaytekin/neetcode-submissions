class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        index = 0
        count = 0
        max_count = 0
        while index < n:
            if count == 0:
                head = nums[index]
                count = 1
            elif nums[index] == head + count:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
                head = nums[index]
            index += 1
        return max(max_count, count)