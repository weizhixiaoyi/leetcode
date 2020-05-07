// Created by Eric on 2020/5/7.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 转置 + 行翻转
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
//        cout << matrix.size() << endl;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (i > j){
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }
        }
        for (int i = 0; i < matrix.size(); i++){
            vector<int> line = matrix[i];
            for (int j = 0; j < matrix[i].size(); j++){
                matrix[i][j] = line[matrix[i].size() - j - 1];
            }
        }
//        for (int i = 0; i < matrix.size(); i++){
//            for (int j = 0; j < matrix[0].size(); j++){
//                cout << matrix[i][j] << " ";
//            }
//            cout << endl;
//        }

    }
};

int main(){
    vector<vector<int>> matrix{
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
    };
    Solution solution;
    solution.rotate(matrix);
}