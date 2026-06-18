class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int[] A;
        int[] B;
        if (nums1.length <= nums2.length){
            A = nums1;
            B = nums2;
        }else{
            A = nums2;
            B = nums1;
        }
        int n = A.length;
        int m = B.length;
        int startA = 0;
        int endA = A.length;
        while (true){
            int i = (startA+endA)/2;
            int j = (n+m+1)/2 -i;
            int leftA = i > 0 ? A[i-1] : Integer.MIN_VALUE;
            int rightA = i <= A.length-1 ? A[i] : Integer.MAX_VALUE;
            int leftB = j > 0 ? B[j-1] : Integer.MIN_VALUE;
            int rightB = j <= B.length-1 ? B[j] : Integer.MAX_VALUE;
            if (leftA <= rightB && leftB <= rightA){
                if ((n+m)%2 == 1){
                   return Math.max(leftA, leftB);
                }else{
                    return  ((Math.max(leftA, leftB)+Math.min(rightA,rightB))/2.0);
                }
            }else if (leftA> rightB){
                endA = i-1;
            }else{
                startA = i+1;
            }
            
        }

        
    }
}