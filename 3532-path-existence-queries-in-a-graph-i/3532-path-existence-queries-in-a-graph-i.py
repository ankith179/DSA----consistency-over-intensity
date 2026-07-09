from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        compNo = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                compNo += 1
            component[i] = compNo
            
        return [component[q[0]] == component[q[1]] for q in queries]