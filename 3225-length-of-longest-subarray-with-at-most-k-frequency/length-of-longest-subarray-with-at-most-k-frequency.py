class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_len =0
        left =0
        counts ={}

        for right in range(len(nums)):
            curr = nums[right]
            if curr in counts:
                counts[curr] +=1
            else:
                counts[curr] = 1
            
            while counts[curr] > k:
                left_slide = nums[left]
                counts[left_slide] -=1
                left +=1

            window_len = right - left +1
            if window_len > max_len:
                max_len = window_len
        return max_len


        