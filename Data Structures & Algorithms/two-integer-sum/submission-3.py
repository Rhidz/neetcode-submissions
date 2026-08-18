class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target_indices = ()
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                temp_sum = nums[i] + nums[j]
                if temp_sum == target:
                    target_indices = [i,j]
                    return target_indices
                j += 1
            
            
        





