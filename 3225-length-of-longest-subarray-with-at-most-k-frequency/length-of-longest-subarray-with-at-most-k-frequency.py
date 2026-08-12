class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            curr = nums[right]
            
            if curr in count:
                count[curr] += 1
            else:
                count[curr] = 1

            while count[curr] > k:
                left_num = nums[left]
                count[left_num] -= 1
                left += 1

            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len