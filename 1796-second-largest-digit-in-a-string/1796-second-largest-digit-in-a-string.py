class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        
        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit > first:
                    second = first
                    first = digit
                elif first > digit > second:
                    second = digit
                    
        return second