// Created by Eric on 2020/5/7.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums) {
        vector<int> L, R;
        int L_product = 1; L.push_back(L_product);
        for (int i = 1; i < nums.size(); i++){
            L_product = L_product * nums[i - 1];
            L.push_back(L_product);
        }
        int R_product = 1; R.push_back(R_product);
        for (int i = nums.size() - 2; i >= 0; i--){
            R_product = R_product * nums[i + 1];
            R.push_back(R_product);
        }
        reverse(R.begin(), R.end());
//        for (int i = 0; i < R.size(); i ++){
//            cout << R[i] << " ";
//        }
//        cout << endl;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            res.push_back(L[i] * R[i]);
        }
        return res;
    }
};

int main() {
    vector<int> a = {1, 2, 3, 4};
    Solution solution;
    vector<int> res = solution.productExceptSelf(a);
    for (int i = 0; i < res.size(); i++){
        cout << res[i] << " ";
    }
    cout << endl;
}


