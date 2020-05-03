// Created by Eric on 2020/5/3.

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int> &nums) {
        map<int, int> occur;
        map<int, int>::iterator iter;
        for (int i = 0; i < nums.size(); i++){
            iter = occur.find(nums[i]);
            if (iter == occur.end()){
                occur.insert(pair<int, int>(nums[i], 1));
            }
        }
        vector<int> res;
        map<int, int>::iterator iter_s;
        for (int i = 1; i <= nums.size(); i++){
            iter_s = occur.find(i);
            if (iter_s == occur.end()){
                res.push_back(i);
            }
        }
        return res;
    }
};

int main() {
    int b[2] = {1, 1};
    vector<int> a(b, b + 2);
    Solution solution;
    vector<int> res = solution.findDisappearedNumbers(a);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
}
