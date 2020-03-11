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
    int diameterOfBinaryTree(TreeNode* root) {

    }

    int maxdiameter(TreeNode *root, int &res){
        if (root == NULL){
            return 0;
        }

        int left = diameterOfBinaryTree(root->left) + 1;
        int right = diameterOfBinaryTree(root->right) + 1;

        if (root->left == root->right) {
            res = left + right;
        }

        return max(left + right, res);
    }
};

int main(){
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    auto *l15 = new TreeNode(5);

}