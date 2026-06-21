class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length-1;
        int vol = Math.min(height[i],height[j]) * (j-i);
        int testvol = 0;
        while (i < j){
            if (height[i] <= height[j]){
                i++;
            }else{
                j--;
            }

            testvol = Math.min(height[i],height[j]) * (j-i);
            if ( testvol > vol){
            
            vol = testvol;
            }

        }

        return vol;


        
    }
}