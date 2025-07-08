class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        r = 0
        digits[i]+=1
        while i >= 0:
            digits[i]+=r
            r=0
            if digits[i] >= 10:
                r = digits[i] // 10
                digits[i] = digits[i] % 10
            i-=1

        if r > 0:
            head = [r]
            head.extend(digits)
            return head

        return digits

            
        