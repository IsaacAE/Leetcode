class Solution:
    def isValid(self, s: str) -> bool:
        dict_paren= {"(":1, ")":-1, "[":2, "]":-2, "{":3, "}":-3}
        stack = []

        for paren in s:
            current = dict_paren.get(paren)
            if  current > 0:
                stack.append(paren)
            else:
               if not stack:
                    return False
               pair = dict_paren.get(stack.pop())

               if pair + current != 0:
                    return False

        if len(stack) > 0:
            return False
        
        return True
               
