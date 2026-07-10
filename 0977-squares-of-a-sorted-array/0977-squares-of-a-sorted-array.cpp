class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int>result(nums.size());
        int left=0;
        int right=nums.size()-1;
        int k=nums.size()-1;
        while (left<=right){
            if (abs(nums[left])>abs(nums[right])){

                result[k]= nums[left] * nums[left];
                left+=1;
            
            }
            else{
                result[k]=nums[right]*nums[right];
                right-=1;
                
            }
            k-=1;


        }return result;
    }
};