class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int XOR_all=0;
        for (int i=0;i<=nums.size();i++){
            XOR_all^=i;
        }
        for (int num :nums){
            XOR_all^=num;
        }
        return XOR_all;
    }
};