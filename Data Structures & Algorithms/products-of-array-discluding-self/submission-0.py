class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_array = []
        right_array = []

        for i in range(len(nums)):
            if i ==0: 
                left_array.append(1)
            else:
                left_array.append(nums[i-1]*left_array[i-1])
        
        i =0 

        for j in range(len(nums)-1,-1,-1):

            if j == len(nums)-1: right_array.append(1)
            else: 
                right_array.append(nums[j+1]*right_array[i-1])
            i+=1
        right_array = right_array[::-1]
        ret = []
        for i in range(len(right_array)):
            ret.append(right_array[i]*left_array[i])
        return ret

        