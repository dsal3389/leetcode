from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        steps_count = 0 

        for c in t:
            if c not in s_count or s_count[c] <= 0:
                steps_count += 1
            s_count[c] -= 1
        return steps_count
