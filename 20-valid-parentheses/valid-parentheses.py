class Solution:
    def isValid(self, s: str) -> bool:
        dict_paren= {")":"(", "]":"[", "}":"{"}
        stack = []

        for paren in s:
            current = dict_paren.get(paren)
            if current != None:
                if not stack or stack.pop() != current:
                    return False
            else:
                stack.append(paren)

        if len(stack) > 0:
            return False
        
        return True
               
