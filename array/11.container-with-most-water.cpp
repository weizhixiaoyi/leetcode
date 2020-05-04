// Created by Eric on 2020/5/4.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        // way1
//        int max_res = 0;
//        for (int i = 0; i < height.size() - 1; i++){
//            for (int j = i + 1; j < height.size(); j++){
//                int cur = min(height[i], height[j]);
//                int cur_res = cur * (j - i);
//                if (cur_res > max_res){
//                    max_res = cur_res;
//                }
//            }
//        }
//        return max_res;
        // way2: 利用双指针，每次移动最短的那个指针
        int max_res = 0;
        for (int i = 0, j = height.size() - 1;;) {
            if (i >= j) {
                break;
            }
            int cur = min(height[i], height[j]);
            int cur_res = cur * (j - i);
//            cout << cur << " " << cur_res << endl;
            if (cur_res > max_res) max_res = cur_res;
            if (height[i] <= height[j]) {
                i += 1;
            } else if (height[i] > height[j]) {
                j -= 1;
            }
        }
        return max_res;
    }
};

int main() {
    int a[9] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    vector<int> b(a, a + 9);
    Solution solution;
    int res = solution.maxArea(b);
    cout << "res: " << res << endl;
}