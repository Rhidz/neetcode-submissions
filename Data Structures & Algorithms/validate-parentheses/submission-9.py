class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if self.isOpening(char):
                stack.append(char)
            
            elif stack and self.isClosing(char):
                currentItem = stack.pop()

                if (currentItem == "[" and char == "]") or (currentItem == "(" and char == ")") or (currentItem == "{" and char == "}"):
                    continue
                else:
                    return False
            else: return False
        
        return True if not stack else False
            
  
    def isOpening(self, c):
        # return c in ("(", "{", "[")
        return True if c == "(" or c == "{" or c == "[" else False
    
    def isClosing(self, c):
        return c in (")", "}", "]")
        
        
        