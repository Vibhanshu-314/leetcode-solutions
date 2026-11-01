/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left=0;
    let right=height.length-1
    let max_water=0;
    while (left<right){
        let current_water=Math.min(height[left],height[right])*(right-left);
        max_water=Math.max(current_water,max_water);
        if (height[left]>height[right]){
            right--;
        }
        else {
            left++;
        }
    }
    return max_water;
};