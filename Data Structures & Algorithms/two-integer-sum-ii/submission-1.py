class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        big = len(numbers) - 1
        current = numbers[small] + numbers[big]
        while current != target:
            if current < target:
                small += 1
            else:
                big -= 1
            current = numbers[small] + numbers[big]
        return [small+1, big+1]