// Created by Eric on 2020/5/9.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 重点在于审题。
// 定义状态, 根据状态寻找转移方式。
class Solution {
public:
    int rob(vector<int> &nums) {
        int nums_size = nums.size();
        if (nums_size == 0) {
            return 0;
        } else if (nums_size == 1) {
            return nums[0];
        } else if (nums_size == 2) {
            return max(nums[0], nums[1]);
        } else {
            vector<int> dp(nums_size);
            dp[0] = nums[0];
            dp[1] = max(nums[0], nums[1]);
            for (int i = 2; i < nums_size; i++) {
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);
            }
//            for (int i = 0; i < nums_size; i++){
//                cout << dp[i] << " ";
//            }
//            cout << endl;
            return dp[nums_size - 1];
        }
    }
};

int main() {
    vector<int> nums = {1, 2, 3, 1};
    Solution solution;
    int res = solution.rob(nums);
    cout << "res: " << res << endl;
}