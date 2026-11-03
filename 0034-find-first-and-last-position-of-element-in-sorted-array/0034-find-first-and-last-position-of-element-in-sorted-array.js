/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    
    function findFirst(){
        let first=-1;
        let left=0;
        let right=nums.length-1;

        while (left<=right){
            let mid=Math.floor((left+right)/2);

            if (nums[mid]===target){
                   first=mid;
                   right=mid-1;

            }
            else if(nums[mid]<target){
                left=mid+1;
            }

            else {
                right=mid-1;
            }
        }
        return first;
    }
    
    function findLast(){
        let last=-1;
        let left=0;
        let right=nums.length-1;

        while (left<=right){
            let mid=Math.floor((left+right)/2);

            if (nums[mid]===target){
                   last=mid;
                   left=mid+1;

            }
            else if(nums[mid]<target){
                left=mid+1;
            }

            else {
                right=mid-1;
            }
        }
        return last;
    }   
    return [findFirst(),findLast()]; 

    
};