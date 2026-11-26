class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [[i, j]
            for i in range(len(nums)) if (target - nums[i]) in set(nums[i+1:])
            for j in [nums[i+1:].index(target-nums[i])+i+1]
            ][0]