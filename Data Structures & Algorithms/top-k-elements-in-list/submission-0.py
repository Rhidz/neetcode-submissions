class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # make a dictionary with the nums 
        dics  = {}
        
        for num in nums:
            if num not in dics.keys():
                dics[num] = 1 # this is the first time seeing it
            else: 
                dics[num] += 1
        
        return sorted(dics, key=dics.get, reverse=True)[:k]

        
        

        