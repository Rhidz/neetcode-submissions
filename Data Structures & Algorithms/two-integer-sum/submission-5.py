class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dics = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in dics.keys():
                return [dics[target-nums[i]], i]
            else:
                #store the index
                dics[nums[i]] = i
                
            
     



