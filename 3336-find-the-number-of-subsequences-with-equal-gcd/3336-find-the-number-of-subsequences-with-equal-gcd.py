class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        mx = max(nums)
        
        dp = [[0] * (mx + 1) for _ in range(mx + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [[0] * (mx + 1) for _ in range(mx + 1)]
            for gcd1 in range(mx + 1):
                new_gcd1 = math.gcd(gcd1, num)
                for gcd2 in range(mx + 1):
                    ways = dp[gcd1][gcd2]
                    if ways == 0:
                        continue
                    
                    new_gcd2 = math.gcd(gcd2, num)
                    
                    new_dp[gcd1][gcd2] = (new_dp[gcd1][gcd2] + ways) % mod
                    new_dp[new_gcd1][gcd2] = (new_dp[new_gcd1][gcd2] + ways) % mod
                    new_dp[gcd1][new_gcd2] = (new_dp[gcd1][new_gcd2] + ways) % mod
            dp = new_dp
            
        ans = 0
        for gcd_val in range(1, mx + 1):
            ans = (ans + dp[gcd_val][gcd_val]) % mod
            
        return ans