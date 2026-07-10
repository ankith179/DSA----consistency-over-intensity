import math
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        point = {orig_idx: sorted_idx for sorted_idx, (_, orig_idx) in enumerate(sorted_nums)}
        
        up = [0] * (n + 1)
        j = 0
        for i in range(n):
            while j + 1 < n and (sorted_nums[j + 1][0] - sorted_nums[i][0]) <= maxDiff:
                j += 1
            if j < i:
                j = i
            up[i] = j
            
        k = math.floor(math.log2(n)) + 1 if n > 0 else 1
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = up[i]
            
        for j in range(1, k):
            for i in range(n):
                dp[i][j] = dp[dp[i][j - 1]][j - 1]
                
        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
                
            st = min(point[u], point[v])
            en = max(point[u], point[v])
            
            if up[st] == st:
                res.append(-1)
                continue
                
            node = st
            step = 0
            
            for i in range(k - 1, -1, -1):
                if dp[node][i] < en:
                    node = dp[node][i]
                    step += (1 << i)
                    
            if up[node] < en:
                res.append(-1)
            else:
                res.append(step + 1)
                
        return res