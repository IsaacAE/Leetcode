class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length-1;
        int vol = Math.min(height[i],height[j]) * (j-i);
        while (i < j){
            if (height[i] <= height[j]){
                i++;
               
                    
                    if (Math.min(height[i],height[j]) * (j-i) > vol){
                   
                    vol = Math.min(height[i],height[j]) * (j-i);
                    }
                
            }else{
                j--;
                
                    if (Math.min(height[i],height[j]) * (j-i) > vol){
                     vol = Math.min(height[i],height[j]) * (j-i);
                    }
                

            }

        }

        return vol;


        
    }
}