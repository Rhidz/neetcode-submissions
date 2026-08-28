class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dics = {}

        for i in range(len(numbers)):
            key = target - numbers[i]
            if key in dics.keys():
                return([dics[key] + 1, i+1])
                
            else: 
                dics[numbers[i]] = i