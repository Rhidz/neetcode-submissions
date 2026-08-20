class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            
            while  s[j] != "#" :
                j += 1
            
            print(s[i:j])
            length = int(s[i:j])
            string = s[j + 1 : j + 1 + length] # s[ j+2 : length] will this work?
            res.append(string)
            i = j + 1 + length
        
        return res

