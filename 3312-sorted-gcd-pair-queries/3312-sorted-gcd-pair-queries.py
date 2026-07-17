class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        cnt_multiples = [0] * (max_val + 1)
        for x in range(1, max_val + 1):
            for multiple in range(x, max_val + 1, x):
                cnt_multiples[x] += counts[multiple]
                
        gcd_count = [0] * (max_val + 1)
        for x in range(max_val, 0, -1):
            c = cnt_multiples[x]
            total_pairs = c * (c - 1) // 2
            
            for multiple in range(2 * x, max_val + 1, x):
                total_pairs -= gcd_count[multiple]
                
            gcd_count[x] = total_pairs
            
        prefix_sums = [0] * (max_val + 1)
        for x in range(1, max_val + 1):
            prefix_sums[x] = prefix_sums[x - 1] + gcd_count[x]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans