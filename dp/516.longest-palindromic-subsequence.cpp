// Created by Eric on 2020/5/12.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int len = s.length();
        if (len == 0) return 0;
        string s1 = s;
        string s2 = s; reverse(s2.begin(), s2.end());
        vector<vector<int>> dp(len + 1, vector<int>(len + 1, 0));
        for (int i = 1; i <= len; i++){
            for (int j = 1; j <= len; j++){
                if (s1[i - 1] == s2[j - 1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
                else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[len][len];
    }
};

int main(){
    string s;
    Solution solution;
    while(true){
        cin >> s;
        int res = solution.longestPalindromeSubseq(s);
        cout << "res: " << res << endl;
    }
}
