class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        n = len(nums)
        unique = 1
        current = nums[0]
        for i in range(1, n):

            if current < nums[i]:
                current = nums[i]
                nums[unique]= current
                unique += 1
        return unique
        
            
        






        