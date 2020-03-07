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

class Solution {
public:
//    bool isSymmetric(TreeNode *root) {
//        if (root == NULL) {
//            return true;
//        }
//        return same(root, root);
//    }
//
//    // 函数定义, 两个节点, 比较后返回true or false;
//    bool same(TreeNode *root1, TreeNode *root2) {
//
//        // 递归结束条件
//        if (root1 == NULL && root2 == NULL) {
//            return true;
//        }
//        if (root1 && root2 == NULL) {
//            return false;
//        }
//        if (root1 == NULL && root2) {
//            return false;
//        }
//        if (root1->val != root2->val) {
//            return false;
//        }
//
//        // 递归等价关系
//        bool left = same(root1->left, root2->right);
//        if (!left) {
//            return false;
//        }
//        bool right = same(root1->right, root2->left);
//        if (!right) {
//            return false;
//        }
//
//        return true;
//    }

    // 每两个元素出来的值相同
    bool isSymmetric(TreeNode *root) {
        queue<TreeNode*> q;

        q.push(root); q.push(root);
        while(!q.empty()){
            TreeNode *t1 = q.front(); q.pop();
            TreeNode *t2 = q.front(); q.pop();

            if (t1 == NULL && t2 == NULL) continue;
            if (t1 == NULL || t2 == NULL) return false;
            if (t1->val != t2->val) return false;

            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }

        return true;
    }
};

int main() {
    TreeNode *root = new TreeNode(1);
    TreeNode *r11 = new TreeNode(2);
    TreeNode *r12 = new TreeNode(2);
    TreeNode *r21 = new TreeNode(3);
    TreeNode *r22 = new TreeNode(4);
    TreeNode *r23 = new TreeNode(4);
    TreeNode *r24 = new TreeNode(4);

    root->left = r11;
    root->right = r12;
    r11->left = r21;
    r11->right = r22;
    r12->left = r23;
    r12->right = r24;

    Solution solution;
    bool result = solution.isSymmetric(root);
    cout << result << endl;
}

//int f(int n) {
////    int sum = 1;
//
//    if (n == 1) {
//        return 1;
//    } else {
//        return n * f(n - 1);
//    }
//}
//
//int main() {
//    cout << f(5) << endl;
//}