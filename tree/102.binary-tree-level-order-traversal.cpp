// Created by Eric on 2020/3/11.

#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Solution {
public:
    // bfs
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> res;
        if (root == nullptr) {
            return res;
        }

        queue<TreeNode *> q; q.push(root);
        while (!q.empty()) {
            vector<int> level;
            int count = q.size();
            // bfs方法依次处理每一次, 对当前层元素进行记录, 然后截断处理。
            while (count--) {
                auto *cur = q.front(); q.pop();
                level.push_back(cur->val);
                if (cur->left != nullptr) {
                    q.push(cur->left);
                }
                if (cur->right != nullptr) {
                    q.push(cur->right);
                }
            }
            res.push_back(level);
        }
        return res;
    }
    // dfs
//    vector<vector<int>>  res;
//    vector<vector<int>> levelOrder(TreeNode *root) {
//        cal(root, 0);
//        return res;
//    }
//    void cal(TreeNode *root, int level){
//        if (root == nullptr) {
//            return;
//        }
//        if (res.size() == level) {
//            res.resize(level + 1);
//        }
//        res[level].push_back(root->val);
//        cal(root->left, level + 1);
//        cal(root->right, level + 1);
//    }
};

int main() {
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    auto *l15 = new TreeNode(5);


    l11->left = l12;
    l11->right = l13;
    l13->left = l14;
    l14->right = l15;

    Solution solution;
    vector<vector<int>> res = solution.levelOrder(l11);
    for (int i = 0; i < res.size(); i++) {
        for (int j = 0; j < res[i].size(); j++) {
            cout << res[i][j] << " ";
        }
        cout << endl;
    }
}