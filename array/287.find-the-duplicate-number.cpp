// Created by Eric on 2020/5/4.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) return nums[i];
        }
    }
};

int main() {
    int a[5] = {1, 3, 4, 2, 2};
    vector<int> b(a, a + 5);
    Solution solution;
    int res = solution.findDuplicate(b);
    cout << "res: " << res << endl;
}