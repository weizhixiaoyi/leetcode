// Created by Eric on 2020/5/9.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0){
                    dp[i][j] = 1;
                }
                if (i ==0 && j != 0){
                    dp[i][j] = 1;
                }
                if (i != 0 && j == 0){
                    dp[i][j] = 1;
                }
                if (i != 0 && j != 0){
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
//        for (int i = 0; i < n; i++){
//            for (int j = 0; j < m; j++){
//                cout << dp[i][j] << " ";
//            }
//            cout << endl;
//        }
        return dp[n - 1][m - 1];
    }
};

int main() {
    int m = 3, n = 2;
    Solution solution;
    int res = solution.uniquePaths(m, n);
    cout << "res: " << res << endl;
}


