class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n-1
        diff = 0

        while i <= j:
            if nums[i] == val:
                
                if nums[j] == val:
                    j-=1
                else:
                    diff +=1
                    nums[i] = nums[j]
                    j-=1
                    i+=1
            else:
                diff +=1 
                i+=1  
                
        return diff
        