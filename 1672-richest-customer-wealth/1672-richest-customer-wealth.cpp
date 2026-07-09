class Solution{
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int richest=0;
        for ( vector<int> account : accounts){
            int wealth=0;
            for( int i =0;i<account.size();i++){
                wealth+=account[i];

                

            }
            richest=max(richest,wealth);

        }
        return richest;
    }
};