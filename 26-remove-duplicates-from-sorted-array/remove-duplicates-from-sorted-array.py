class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        unique = 1
        current = nums[0]
        for i in range(1,n):

            if current < nums[i]:
                current = nums[i]
                nums[unique]= current
                unique += 1

        for j in range(unique, n):
            nums[j] = "_"

        return unique
        
            
        






        