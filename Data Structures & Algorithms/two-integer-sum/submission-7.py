class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # take a hashmap or dictionary
        dics = {}

        for i in range(len(nums)):
            key = target - nums[i]
            if key in dics.keys():
                return [dics[key], i]
            else:
                #store the index
                dics[nums[i]] = i
        


        
            
     



