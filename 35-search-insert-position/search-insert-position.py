class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start+end) // 2
        reach = True

        while start < end:
            
            search = nums[mid]
            if search == target:
                return mid
            
            if search < target:
                start = mid+1
            
            elif search > target:
                end = mid-1

            else:
                end = mid-1

            mid = (start+end) // 2

            

        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end

        if nums[mid] > target and target > nums[start]:
            return mid-1

        if nums[mid] > target and target < nums[start]:
            return start
        
        if nums[mid] < target and target < nums[end]:
            return mid+1
        else:
            return end+1
                 
        