from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)
        operations_count = 0

        for n in nums:
            nums_count[n] += 1
        
        for n, c in nums_count.items():
            if c == 1:
                return -1

            operations_count += (c // 3)
            
            if c % 3 != 0:
                operations_count += 1 
        return operations_count

        