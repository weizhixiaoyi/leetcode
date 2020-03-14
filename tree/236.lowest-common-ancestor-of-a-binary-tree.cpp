// Created by Eric on 2020/3/14.

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

// HINT
// 理解递归真正的含义, 里面是用栈进行存储, 可以联想树的三种遍历方式, 每种方式存储和遍历的特点。
// 本题之所以开始没有想到，是因为不知道如何处理两个节点的问题。递归的理解从下到上的方式没有理解清楚。
// 本题核心点在于，要记录该节点的左、右、自己是否和需查找值相等。记录该条路径上是否存在需查找值。利用||可以很好的处理此点，记录路径上是否存在。
// 薄弱点：递归的理解不清楚，返回值不清楚。

class Solution {
public:
    TreeNode *res = nullptr;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        isInclude(root, p, q);
//        cout << res->val << endl;
        return res;
    }

    bool isInclude(TreeNode *root, TreeNode *p, TreeNode *q) {
        if (root == nullptr) {
            return false;
        }

        bool left = isInclude(root->left, p, q);
        bool right = isInclude(root->right, p, q);

        bool equal = false;
        if (root == p || root == q) {
            equal = true;
        }
        if ((left && right) || (left && equal) || (right && equal)) {
            res = root;
        }

        return left || right || equal;
    }
};

int main() {
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    auto *l15 = new TreeNode(5);

    l11->left = l12;
    l11->right = l13;
    l12->left = l14;
    l12->right = l15;

    Solution solution;
    TreeNode *result = solution.lowestCommonAncestor(l11, l14, l15);
    cout << result->val << endl;
}