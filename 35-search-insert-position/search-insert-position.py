class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
    
        while start <= end:
            mid = (start+end) // 2
            search = nums[mid]
            if search == target:
                return mid   
            elif search < target:
                start = mid+1
            else:
                end = mid-1
  
        return start
        