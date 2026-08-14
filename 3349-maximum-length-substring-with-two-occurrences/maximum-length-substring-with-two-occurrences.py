class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            curr = s[right]
            
            if curr in count:
                count[curr] += 1
            else:
                count[curr] = 1

            while count[curr] > 2:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len