// Created by Eric on 2020/5/4.
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int> &nums) {
//        int min_index = nums.size(), max_index = 0;
//        for (int i = 0; i < nums.size() - 1; i++) {
//            for (int j = i + 1; j < nums.size(); j++) {
//                if (nums[j] < nums[i]) {
//                    min_index = min(i, min_index);
//                    max_index = max(j, max_index);
//                }
//            }
//        }
//        return max_index - min_index < 0 ? 0 : max_index - min_index + 1;
// way2
        int nums_size = nums.size();
        if (nums_size <= 1) return 0;
        int max_value = nums[0], max_index = 0;
        int min_value = nums[nums_size - 1], min_index = nums_size - 1;
        for (int i = 1; i < nums.size(); i++){
            max_value = max(max_value, nums[i]);
            min_value = min(min_value, nums[nums_size - i - 1]);
            if (nums[i] < max_value) max_index = i;
            if (nums[nums_size - i - 1] > min_value) min_index = nums_size - i - 1;
        }
//        cout << max_index << " " << min_index << endl;
        return max_index - min_index < 0 ? 0: max_index - min_index + 1;
    }
};

int main() {
    int a[5] = {1, 2, 3, 5, 4};
    vector<int> b(a, a + 5);
    Solution solution;
    int res = solution.findUnsortedSubarray(b);
    cout << "res: " << res << endl;
}
