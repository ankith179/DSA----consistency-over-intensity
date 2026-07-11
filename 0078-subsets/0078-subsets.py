class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        op = []
        
        def solve(start: int):
            if start == len(nums):
                res.append(list(op))
                return
            
            solve(start + 1)
            
            op.append(nums[start])
            solve(start + 1)
            op.pop()
            
        solve(0)
        return res