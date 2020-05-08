// Created by Eric on 2020/5/8.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        if (n == 2){
            return 2;
        }
        if (n >= 3){
            vector<int> dp(n + 1, 0);
            dp[1] = 1; dp[2] = 2;
            for (int i = 3; i <= n; i ++){
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            return dp[n];
        }
    }
};

int main(){
    int n = 1;
    Solution solution;
    int res = solution.climbStairs(n);
    cout << "res: " << res << endl;
}