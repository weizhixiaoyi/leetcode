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
    int maxDepth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }

        // 递进过程, 中间信息需要存储起来, 需要栈的花销.
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);

        // 归并过程, 将栈里面信息计算出来.
        return max(left, right) + 1;
    }

    bool depth(TreeNode *root, int &res) {
        if (root == NULL) return false;

//        bool left = true, right = true;


        bool left = depth(root->left, res);
        bool right = depth(root->right, res);
//        if (root->left) {
//
//        }
//        if (root->right) {
//
//        }
//        cout << res << endl;
        //
        cout << "left: " << depth(root->left, res) << endl;
        cout << "right: " << depth(root->left, res) << endl;
//        if (left || right){
//            res += 1;
//            cout << res << endl;
//        }
    }
};

int main() {
    TreeNode *root = new TreeNode(1);
    TreeNode *r11 = new TreeNode(2);
    TreeNode *r12 = new TreeNode(3);
    TreeNode *r21 = new TreeNode(4);
    TreeNode *r22 = new TreeNode(5);
    TreeNode *r23 = new TreeNode(6);
    TreeNode *r24 = new TreeNode(7);

    root->left = r11;
    root->right = r12;
    r11->left = r21;
    r11->right = r22;
    r12->left = r23;
    r12->right = r24;


    Solution solution;
    int result = solution.maxDepth(root);
    cout << result << endl;
}