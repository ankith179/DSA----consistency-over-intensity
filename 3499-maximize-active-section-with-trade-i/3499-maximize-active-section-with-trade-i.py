class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        base_ones = s.count('1')
        
        zero_lengths = []
        curr_zero_count = 0
        
        for char in t:
            if char == '0':
                curr_zero_count += 1
            else:
                if curr_zero_count > 0:
                    zero_lengths.append(curr_zero_count)
                    curr_zero_count = 0
                    
        if len(zero_lengths) < 2:
            return base_ones
            
        max_delta = 0
        for i in range(len(zero_lengths) - 1):
            max_delta = max(max_delta, zero_lengths[i] + zero_lengths[i + 1])
            
        return base_ones + max_delta