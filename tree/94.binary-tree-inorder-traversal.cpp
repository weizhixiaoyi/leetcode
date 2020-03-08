// Created by Eric on 2020/3/8.

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
    // 1.递归方法
//    vector<int> inorderTraversal(TreeNode* root) {
//        vector<int> result;
//        inorder(root, result);
//
//        return result;
//    }
//
//    void inorder(TreeNode *root, vector<int> &result){
//        if (root == NULL){
//            return;
//        }
//
//        inorder(root->left, result);
//        result.push_back(root->val);
//        inorder(root->right, result);
//    }

    // 循环方法
    // Hint: 利用栈来存储左节点, 左节点为空时, 元素进行出栈, 依次加入右边元素.
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        stack<TreeNode *> s;
        TreeNode *temp = root;
        while (!s.empty() || temp != nullptr) {
            while (temp != nullptr) {
                s.push(temp);
                temp = temp->left;
            }
            temp = s.top(); s.pop();
            result.push_back(temp->val);
            temp = temp->right;
        }
        return result;
    }
};

int main() {
    TreeNode *r11 = new TreeNode(1);
    TreeNode *r12 = new TreeNode(2);
    TreeNode *r13 = new TreeNode(3);
    TreeNode *r14 = new TreeNode(4);
    TreeNode *r15 = new TreeNode(5);
    TreeNode *r16 = new TreeNode(6);
    TreeNode *r17 = new TreeNode(7);

    r11->left = r12;
    r11->right = r13;
    r12->left = r14;
    r12->right = r15;
    r13->left = r16;
    r13->right = r17;

    Solution solution;
    vector<int> result = solution.inorderTraversal(r11);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
}