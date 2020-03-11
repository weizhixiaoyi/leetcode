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


// 树的层次遍历
void PrintTree(TreeNode *root) {
    TreeNode *temp = root;
    queue<TreeNode *> q;
    q.push(temp);

    while (!q.empty()) {
        TreeNode *cur = q.front();
        q.pop();

        cout << cur->val << " ";
        if (cur->left) {
            q.push(cur->left);
        }
        if (cur->right) {
            q.push(cur->right);
        }
    }
    cout << endl;
}

class Solution {
public:
    void flatten(TreeNode* root) {
        while (root != nullptr){
            if (root->left == nullptr){
                root = root->right;
            } else {
                // 找到左子树的最右边节点
                TreeNode *prev = root->left;
//                cout << prev->val << endl;
                while (prev->right != nullptr){
                    prev = prev->right;
                }

                // 将右子树接到左子树的最右边节点
                prev->right = root->right;

                // 左右子树互换
                root->right = root->left;

                root->left = nullptr;
                root = root->right;
            }
        }
    }
};

int main() {
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    l11->left = l12;
    l12->left = l13;
    l12->right = l14;
    PrintTree(l11);

    Solution solution;
    solution.flatten(l11);
}
