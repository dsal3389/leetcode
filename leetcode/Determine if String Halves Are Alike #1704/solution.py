import math

VOWELES = frozenset(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        hand_point_index = math.ceil(len(s) / 2)

        a_index = 0
        b_index = hand_point_index

        a_count = 0
        b_count = 0

        while a_index < hand_point_index:
            if s[a_index] in VOWELES:
                a_count += 1
            if s[b_index] in VOWELES:
                b_count += 1

            a_index += 1
            b_index += 1 
        return a_count == b_count
            
        
