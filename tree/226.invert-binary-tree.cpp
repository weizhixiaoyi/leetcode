// Created by Eric on 2020/3/7.

#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 树的层次遍历
void PrintTree(TreeNode *root){
    TreeNode *temp = root;
    queue<TreeNode*> q;
    q.push(temp);

    while (!q.empty()) {
        TreeNode *cur = q.front(); q.pop();

        cout << cur->val;
        if (cur->left) {
            q.push(cur->left);
        }
        if (cur->right) {
            q.push(cur->right);
        }
    }
    cout << endl;
}

// 解决递归题目三个条件
// 1. 确定function输入和输出是什么, 即定义函数框架
// 2. 确定递归的递进过程的停止条件是什么.
// 3. 递归过程拆解, 分成递进和归并过程, 协同上面两个条件, 确定检查递进和归并条件.
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL){
            return NULL;
        }

        // 递进过程
        TreeNode *left = invertTree(root->left);
        TreeNode *right = invertTree(root->right);

        // 归并过程
        root->left = right;
        root->right = left;
        return root;
    }
};

int main(){
    TreeNode *root = new TreeNode(4);
    TreeNode *r11 = new TreeNode(2);
    TreeNode *r12 = new TreeNode(7);
    TreeNode *r21 = new TreeNode(1);
    TreeNode *r22 = new TreeNode(3);
    TreeNode *r23 = new TreeNode(6);
    TreeNode *r24 = new TreeNode(9);

    root->left = r11;
    root->right = r12;
    r11->left = r21;
    r11->right = r22;
    r12->left = r23;
    r12->right = r24;
    PrintTree(root);

    Solution solution;
    TreeNode *result = solution.invertTree(root);
    PrintTree(result);
}