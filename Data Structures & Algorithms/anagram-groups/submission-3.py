class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dics = {}

        for string in strs:
            freq = [0]*26

            for char in string:
                ascii = ord(char) - 97
                freq[ascii] += 1
            
            freq = tuple(freq)
            if freq not in dics.keys():
                dics[freq] = [string]
            else:
                dics[freq].append(string)
            
        results = []

        for key,value in dics.items():
            results.append(value)
        
        return results

       

       

     
        

         
        





        