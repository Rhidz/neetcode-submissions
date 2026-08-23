class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #temp = []
        #for (i in nums):
            # iterate over the nums array 
            # increment hashamp whenever repetition is found
            # return true if repetition is found 
            # return false if not
        temp = set(nums)
        return True if len(temp)!=len(nums) else False
        