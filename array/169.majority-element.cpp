// Created by Eric on 2020/5/3.

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &nums) {
        map<int, int> m;
        map<int, int>::iterator iter;
        for (int i = 0; i < nums.size(); i++) {
            iter = m.find(nums[i]);
            if (iter != m.end()) {
                m[nums[i]] = m[nums[i]] + 1;
            } else {
                m[nums[i]] = 1;
            }
        }
        int max_times = 0, max_value = 0;
        map<int, int>::iterator iter_s;
        for (iter_s = m.begin(); iter_s != m.end(); iter_s++) {
            if (iter_s->second > max_times){
                max_times = iter_s->second;
                max_value = iter_s->first;
            }
        }
        return max_value;
    }
};

int main() {
    int num[3] = {3, 2, 3};
    vector<int> v(num, num + 3);
    Solution solution;
    int res = solution.majorityElement(v);
    cout << res << endl;
}
