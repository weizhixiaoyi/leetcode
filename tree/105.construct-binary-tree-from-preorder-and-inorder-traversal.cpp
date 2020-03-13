// Created by Eric on 2020/3/13.

#include <iostream>
#include <algorithm>
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
    // 函数需要考虑下标问题，不能够通过此函数进行，另外构建一个函数。
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return Tree(0, 0, int(inorder.size() - 1), preorder, inorder);
    }

    // 函数的接受条件是vector, 下标来表示移动.
    TreeNode* Tree(int preStart, int inStart, int inEnd, vector<int> &preorder, vector<int> &inorder){
        // 考虑变化特征，设计结束条件.
        if (preStart >= preorder.size() || inStart > inEnd) {
            return nullptr;
        }

        TreeNode *root = new TreeNode(preorder[preStart]);
        int index = 0;
        for (int i = inStart; i <= inEnd; i++){
            if (preorder[preStart] == inorder[i]) {
                index = i;
                break;
            }
        }

        // 函数递归构建过程。
        root->left = Tree(preStart + 1, inStart, index - 1, preorder, inorder);
        root->right = Tree(preStart + index - inStart + 1,index + 1,  inEnd, preorder, inorder);
        return root;
    }
};

int main() {
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};

    Solution solution;
    TreeNode *res = solution.buildTree(preorder, inorder);
    PrintTree(res);
}