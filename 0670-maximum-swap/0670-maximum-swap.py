class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        runningMax = "-1"
        indexOfRunningMax = -1
        swap_i = swap_j = -1

        for i in reversed(range(len(nums))):
            if nums[i] > runningMax:
                runningMax = nums[i]
                indexOfRunningMax = i
            elif nums[i] < runningMax:
                swap_i = indexOfRunningMax
                swap_j = i
        
        if swap_i != -1 and swap_j != -1:
            nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]
            
        return int("".join(nums))