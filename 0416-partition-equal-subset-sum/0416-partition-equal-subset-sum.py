class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
            
        haf = total // 2
        dp = [False] * (haf + 1)
        dp[0] = True
        
        for stone in nums:
            for i in range(len(dp) - 1, stone - 1, -1):
                if dp[i - stone]:
                    dp[i] = True
                    
        return dp[haf]
        .0