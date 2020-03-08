// Created by Eric on 2020/3/8.

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

// Hint
// 1. 利用前序遍历
// 2. 递归时候把两棵树相加后的值合并到一棵树上面.
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL){
            return t2;
        }
        if (t2 == NULL){
            return t1;
        }

        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
};

int main(){
    TreeNode *r11 = new TreeNode(1);
    TreeNode *r12 = new TreeNode(3);
    TreeNode *r13 = new TreeNode(2);
    TreeNode *r14 = new TreeNode(5);
    r11->left = r12;
    r11->right = r13;
    r12->left = r14;
    PrintTree(r11);

    TreeNode *r21 = new TreeNode(2);
    TreeNode *r22 = new TreeNode(1);
    TreeNode *r23 = new TreeNode(3);
    TreeNode *r24 = new TreeNode(4);
    TreeNode *r25 = new TreeNode(7);
    r21->left = r22;
    r21->right = r23;
    r22->right = r24;
    r23->right = r25;
    PrintTree(r21);

    Solution solution;
    TreeNode *result = solution.mergeTrees(r11, r21);
    PrintTree(result);
}