import functools

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for text in strs:
            counts = [0 for _ in range(26)]
            for c in text:
                counts[ord(c)-ord('a')] += 1
            groups[tuple(counts)].append(text)
        return list(groups.values())




        