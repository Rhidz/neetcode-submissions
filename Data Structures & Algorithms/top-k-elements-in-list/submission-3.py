class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dics = {}

        for num in nums:
            if num in dics.keys():
                dics[num] += 1
            else:
                dics[num] = 1
        
        return sorted(dics, key=dics.get, reverse=True)[:k]



        # make a dictionary with the nums 
       # since we are sorting the keys not the values





   
            





     

        
        

        