class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        diff = 0

        for num in nums:
            if num != val:
                nums[diff]= num
                diff+=1
                
        return diff
        