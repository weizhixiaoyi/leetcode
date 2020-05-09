// Created by Eric on 2020/5/9.

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int numSquares(int n) {
        // dp
//        int max_square = sqrt(n) + 1;
//        vector<int> squares(max_square, 0);
//        for (int i = 0; i < max_square; i++){
//            squares[i] = i * i;
//        }
//
//        const int INF = 0x3f3f3f;
//        vector<int> dp(n + 1, INF); dp[0] = 0;
//        for (int i = 1; i <= n; i++){
//            for (int j = 1; j < max_square; j++){
//                if (i < squares[j]){
//                    break;
//                }
//                dp[i] = min(dp[i - squares[j]] + 1, dp[i]); // i - squares[j] == 0表示当前i是完全平方数
//            }
//        }
////        for (int i = 1; i <= n; i++){
////            cout << dp[i] << endl;
////        }
//        return dp[n];
        // bfs

    }
};

int main(){
    int n = 13;
    Solution solution;
    int res = solution.numSquares(n);
    cout << "res: " << res << endl;
}


