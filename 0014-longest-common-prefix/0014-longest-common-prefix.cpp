class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty())
            return "";
        sort(strs.begin(),strs.end(),[](string &a,string &b){
            return a.length()<b.length();
        });
        string prefix=strs[0];

        for (int i=0;i<strs.size();i++){
            while (strs[i].find(prefix)!=0){
                prefix.pop_back();

                if (prefix.empty())
                  return "";


            }
        }    
        
        return prefix;
        
    }
};