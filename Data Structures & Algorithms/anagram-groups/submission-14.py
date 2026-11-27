import functools

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for text in strs:
            counts = [0 for _ in range(26)]
            for c in text:
                counts[ord(c)-ord('a')] += 1
            key = tuple(counts)
            if not key in groups:
                groups[key] = []
            groups[key].append(text)
        return list(groups.values())




        