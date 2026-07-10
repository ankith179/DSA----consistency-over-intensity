class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        rob_prev2 = 0
        rob_prev1 = 0
        
        for num in nums:
            current_max = max(rob_prev1, num + rob_prev2)
            rob_prev2 = rob_prev1
            rob_prev1 = current_max
            
        return rob_prev1