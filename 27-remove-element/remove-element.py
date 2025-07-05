class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        diff = 0

        for i in nums:
            if i != val:
                nums[diff]= i
                diff+=1
                
        return diff
        