class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        left = 0
        right = len(numbers) - 1
        current = numbers[left] + numbers[right]
        output = list()
        while left < right:
            if current == target:
                output.append((numbers[left], numbers[right]))
            if current < target:
                left += 1
            else:
                right -= 1
            current = numbers[left] + numbers[right]
        return output
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        output = []
        for i in range(n):
            if i == 0 or nums[i] != nums[i - 1]:
                target = nums[i]
                omitted = nums[i+1:]
                for pair in self.twoSum(omitted, -target):
                    output.append(tuple(sorted([pair[0], pair[1], target])))
        print(output)
        return list(set(output))