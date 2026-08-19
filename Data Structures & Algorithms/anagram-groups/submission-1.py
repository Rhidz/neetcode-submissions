class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through every string in strs
        # make a frequency list for each str
        # add that frequecy list as a key to the dic
        # add the str that matches that frequency list to the dic 

        dic = {}
        for string in strs:
            freq = [0]*26
            for char in string:
                ascii= ord(char)-97
                freq[ascii]+=1
            freq = tuple(freq)
            if freq not in dic.keys():
                dic[freq] = [string]
            else:dic[freq].append(string)
        result = []
        for k,v in dic.items():
            result.append(v)
        return result


        