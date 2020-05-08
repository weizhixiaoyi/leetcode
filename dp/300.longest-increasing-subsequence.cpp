// Created by Eric on 2020/5/8.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int> &nums) {
        int nums_size = nums.size();
        if (nums_size == 1) {
            return 1;
        }

        int ans = 0;
        vector<int> dp(nums_size, 1);
        for (int i = 1; i < nums_size; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 4};
    Solution solution;
    int res = solution.lengthOfLIS(nums);
    cout << "res: " << res << endl;
}