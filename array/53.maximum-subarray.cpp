// Created by Eric on 2020/3/14.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// HINT
// a[i-1]<0, a[i]>0, a[0...i-1] < 0;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, maxSum = nums[0];
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (sum > maxSum) {
                maxSum = sum;
            }

            if (sum < 0) {
                sum = 0;
            }
        }
        return maxSum;
    }
};

int main() {
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    Solution solution;
    int res = solution.maxSubArray(nums);
    cout << res << endl;
}
