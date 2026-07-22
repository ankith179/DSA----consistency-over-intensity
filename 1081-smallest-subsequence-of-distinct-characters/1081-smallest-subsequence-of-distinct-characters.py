class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store the last index of occurrence for each character
        last_index = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If character is already in stack, skip to preserve uniqueness
            if char in seen:
                continue
                
            # Pop characters from stack if they are larger than current char
            # AND will appear again later in s
            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
        