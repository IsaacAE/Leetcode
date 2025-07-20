class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointer = m+n-1
        i = m-1
        j = n-1
       
        while j >= 0 and i >= 0:
            if nums2[j] >= nums1[i]:
                nums1[pointer] = nums2[j]
                j-=1
            else:
                nums1[pointer], nums1[i] = nums1[i], nums1[pointer]
                i-=1
                
            pointer-=1

        i = pointer
        while j >=0:
           
            nums1[i] = nums2[j]
            i-=1
            j-=1
     