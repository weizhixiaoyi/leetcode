// Created by Eric on 2020/5/8.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>> &grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    res[0][0] = grid[0][0];
                }
                if (i == 0 && j > 0) {
                    res[0][j] = grid[0][j] + res[0][j - 1];
                }
                if (i > 0 && j == 0) {
                    res[i][0] = grid[i][0] + res[i - 1][0];
                }
                if (i > 0 && j > 0) {
                    res[i][j] = grid[i][j] + min(res[i - 1][j], res[i][j - 1]);
                }
            }
        }
//        for (int i = 0; i < res.size(); i++){
//            for (int j = 0; j < res[0].size(); j++){
//                cout << res[i][j] << " ";
//            }
//            cout << endl;
//        }
        return res[m - 1][n - 1];
    }
};


int main() {
    vector<vector<int>> grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
    };
    Solution solution;
    int res = solution.minPathSum(grid);
    cout << "res: " << res << endl;
}


