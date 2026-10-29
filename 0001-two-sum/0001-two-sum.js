/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // brute force approach
    // for(let i=0;i<nums.length;i++){
    //     for(let j=i+1;j<nums.length;j++){
    //         if (nums[i]+nums[j]===target){
    //             return [i,j];
    //         };
    //     };
    // };


    //  optimal approach\

    let seen=new Map();
    for (let i=0;i<nums.length;i++){
        let comp=target-nums[i];
        if (seen.has(comp)){
            return [seen.get(comp),i];
        }
        seen.set(nums[i],i);
    }
    
};