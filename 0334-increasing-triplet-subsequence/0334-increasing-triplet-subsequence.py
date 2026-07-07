class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Initialize the first and second elements to infinity
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # num is the smallest so far
            elif num <= second:
                second = num # num is greater than first but smaller than/equal to second
            else:
                # We found a number greater than both first and second
                return True
                
        return False