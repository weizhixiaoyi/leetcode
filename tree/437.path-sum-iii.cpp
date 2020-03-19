// Created by Eric on 2020/3/13.

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
// 将问题转变为层次遍历+从root开始有多少个值为sum的数，最后全部加在一起。
// 层次遍历利用队列是心啊，和为sum利用递归实现。

class Solution {
public:
    int pathSum(TreeNode *root, int sum) {
        if (root == nullptr) {
            return 0;
        }
        queue<TreeNode *> q;
        int res = 0, cur_sum = 0, cur_num = 0;

        q.push(root);
        while (!q.empty()) {
            TreeNode *temp = q.front(); q.pop();
//            cout << temp->val << ":\t";
            Sum(temp, sum, cur_sum, cur_num); res += cur_num;
//            cout << "#\t" << cur_num << endl;
            cur_num = 0;

            if (temp->left) {
                q.push(temp->left);
            }
            if (temp->right) {
                q.push(temp->right);
            }
        }
        return res;
    }

    void Sum(TreeNode *root, int sum, int cur_sum, int &cur_num) {
        if (root == nullptr) {
            return;
        }

        cur_sum += root->val;
//        cout << cur_sum << " ";
        if (cur_sum == sum){
            cur_num += 1;
        }

        Sum(root->left, sum, cur_sum, cur_num);
        Sum(root->right, sum, cur_sum, cur_num);
    }
};

int main() {
    auto *l11 = new TreeNode(10);
    auto *l12 = new TreeNode(5);
    auto *l13 = new TreeNode(-3);
    auto *l14 = new TreeNode(3);
    auto *l15 = new TreeNode(2);
    auto *l16 = new TreeNode(11);
    auto *l17 = new TreeNode(3);
    auto *l18 = new TreeNode(-2);
    auto *l19 = new TreeNode(1);

    l11->left = l12;
    l11->right = l13;
    l12->left = l14;
    l12->right = l15;
    l13->left = l16;
    l14->left = l17;
    l14->right = l18;
    l15->right = l19;
    int sum = 8;

    PrintTree(l11);

    Solution solution;
    int res = solution.pathSum(l11, sum);
    cout << res << endl;
}


