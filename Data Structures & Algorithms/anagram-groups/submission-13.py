import functools

class Solution:
    p = 1000000000000000000000007
    def fastPower(self, base, power):
        if power == 0:
            return 1
        if power == 1:
            return base % self.p
        if power % 2 == 0:
            return self.fastPower(base, power//2)**2 % self.p
        if power % 2 == 1:
            return (self.fastPower(base, power//2)**2 * base) % self.p
    def hsh(self, text):
        power = 2
        for ch in text:
            power = self.fastPower(power, ord(ch)-ord('a')+1)
        return power

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = sorted(strs, key = lambda s: sorted(s))
        output = []
        for s in sorted_list:
            if not output or sorted(output[-1][0]) != sorted(s):
                output.append([])
            output[-1].append(s)
        return output





        