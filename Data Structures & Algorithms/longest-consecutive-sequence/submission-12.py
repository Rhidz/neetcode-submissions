class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        count_so_far= 0
        

        s = set(nums)
        #print(nums)
        if nums == []:return 0

        for i in range(len(nums)):
            if nums[i-1] == nums[i]: 
                #print('I am here')
                continue
            if nums[i]-1 in s:
                count+=1
            
                
                
                

            else:
                count_so_far = max(count,count_so_far)
                
                count=1
            #print(i, count,count_so_far)
        count_so_far = max(count,count_so_far)
        return count_so_far
        

            
        

      

        