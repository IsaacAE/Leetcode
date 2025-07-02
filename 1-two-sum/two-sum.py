class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            search = target-nums[i]
            result = dict.get(search)
            dict.update({nums[i]:i})
            if result is not None :
                index = i
                indexes = [result, index]
                return indexes