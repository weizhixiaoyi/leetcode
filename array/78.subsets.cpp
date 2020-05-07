// Created by Eric on 2020/5/7.

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> N;
        res.push_back(N);
//        cout << res.size() << endl;
        for (int i = 0; i < nums.size(); i++){
            int cur_res_size = res.size();
            for (int j = 0; j < cur_res_size; j++){
                vector<int> cur(res[j]);
                cur.push_back(nums[i]);
                res.push_back(cur);
            }
        }
        return res;
    }
};

int main(){
    vector<int> nums = {1, 2, 3};
    Solution solution;
    vector<vector<int>> res = solution.subsets(nums);
    for (int i = 0; i < res.size(); i++){
        cout << "[";
        for (int j = 0; j < res[i].size(); j++){
           cout << res[i][j] << " ";
        }
        cout << "]" << endl;
    }
}
