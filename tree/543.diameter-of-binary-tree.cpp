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

// HINT
// 当前节点的最大值等于左子树的最高层数+右子树的最高层树.
class Solution {
public:
    int res = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        maxdiameter(root);
        return res;
    }

    int maxdiameter(TreeNode *root){
        if (root == nullptr){
            return 0;
        }

        int lheight = maxdiameter(root->left);
        int rheight = maxdiameter(root->right);
        res = max(res, lheight + rheight);

        return max(lheight, rheight)+ 1;
    }
};

int main(){
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    auto *l15 = new TreeNode(5);

    l11->left= l12;
//    l11->right = l13;
//    l12->left = l14;
//    l12->right = l15;

    Solution solution;
    int res = solution.diameterOfBinaryTree(l11);
    cout << res << endl;
}