class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # let me build the frequency mapper of st
        f_s = [0]*26
        f_t = [0]*26

        for char in s:
            ascii = ord(char)-97
            f_s[ascii] += 1
        
        for char in t:
            ascii = ord(char)-97
            f_t[ascii] += 1
        
        return True if f_s == f_t else False
        
        
