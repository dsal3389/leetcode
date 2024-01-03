
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_count = 0
        total = 0
        
        for plan in bank:
            curr_count = plan.count("1")

            if curr_count > 0:
                total += (prev_count * curr_count)
                prev_count = curr_count
        return total