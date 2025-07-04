class Solution:
    def isValid(self, s: str) -> bool:
        dict_paren= {")":"(", "]":"[", "}":"{"}
        stack = []

        for paren in s:
            if dict_paren.get(paren) != None:
                if not stack or stack.pop() != dict_paren.get(paren):
                    return False
            else:
                stack.append(paren)
                
        if len(stack) > 0:
            return False
        
        return True
               
