class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        small = 0
        big = n - 1
        current = numbers[small] + numbers[big]
        while current != target:
            if current < target:
                small += 1
            else:
                big -= 1
            current = numbers[small] + numbers[big]
        return [small+1, big+1]