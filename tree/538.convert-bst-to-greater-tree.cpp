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

bool cmp(int x, int y){
    return x > y;
}

class Solution {
public:

    TreeNode *convertBST(TreeNode *root) {
        // 得到树中所有元素
        vector<int> num;
        inorder(root, num);

        sort(num.begin(), num.end(), cmp);
        add(root, num);

        return root;
    }

    void add(TreeNode *root, vector<int> &num) {
        if (root == NULL) {
            return;
        }

        add(root->left, num);
        int sum = 0;
        for (int n: num){
            if (n > root->val){
                sum += n;
            } else {
                break;
            }
        }
        root->val += sum;
        add(root->right, num);
    }

    void inorder(TreeNode *root, vector<int> &num) {
        if (root == NULL) {
            return;
        }

        inorder(root->left, num);
        num.push_back(root->val);
        inorder(root->right, num);
    }
};

int main() {
    TreeNode *l11 = new TreeNode(5);
    TreeNode *l12 = new TreeNode(2);
    TreeNode *l13 = new TreeNode(13);
    l11->left = l12;
    l11->right = l13;
    PrintTree(l11);

    Solution solution;
    TreeNode *result = solution.convertBST(l11);
    PrintTree(result);
}