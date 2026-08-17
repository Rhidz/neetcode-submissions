class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target_indices = ()
        dic = {}
        for i in range(len(nums)): 
            if target-nums[i] in dic.keys():
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]] = i
                
            
            
        





