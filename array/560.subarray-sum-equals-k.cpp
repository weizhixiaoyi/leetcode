// Created by Eric on 2020/5/4.

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

// 前缀和 + 哈希表
class Solution {
public:
    int subarraySum(vector<int> &nums, int k) {
        unordered_map<int, int> sum;
        sum[0] = 1;
        int cur_sum = 0, res = 0;
        for (int i = 0; i < nums.size(); i++) {
            cur_sum += nums[i];
            if (sum.find(cur_sum - k) != sum.end()) res += sum[cur_sum - k];
            sum[cur_sum] += 1;
        }
        return res;
    }
};

int main() {
    int a[3] = {1, 1, 1};
    vector<int> b(a, a + 3);
    int k = 2;
    Solution solution;
    int res = solution.subarraySum(b, k);
    cout << "res: " << res << endl;
}