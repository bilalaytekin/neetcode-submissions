class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_int, max_int = -1000, 1000
        counts = [0] * (max_int - min_int + 1)
        for num in nums:
            counts[num - min_int] += 1
        return [
            pair[1]
            for pair
            in sorted(
                [
                    (counts[num - min_int], num)
                    for num
                    in range(min_int, max_int+1)],
                    reverse=True
                    )[:k]
                    ]