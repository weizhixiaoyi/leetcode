// Created by Eric on 2020/3/20.

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <typeinfo>
#include <string>
#include <cstring>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

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
// 树中有重复元素，不能用先序遍历+后序遍历方式求解.
//class Codec {
//public:
//    // Encodes a tree to a single string.
//    string serialize(TreeNode *root) {
//        string preorder_str, inorder_str;
//        preorder_tree(root, preorder_str);
//        inorder_tree(root, inorder_str);
//        return preorder_str + inorder_str;
//    }
//
//
//    // Decodes your encoded data to tree.
//    TreeNode *deserialize(string data) {
//        cout << data << endl;
//        vector<int> preorder_vec, inorder_vec;
//        string cur_str;
//        for (int i = 0; i < data.length(); i++) {
//            if (data[i] == '#') {
//                int cur_val = stoi(cur_str);
////                cout << cur_val << endl;
//                if (i < data.length() / 2) {
//                    preorder_vec.push_back(cur_val);
//                } else {
//                    inorder_vec.push_back(cur_val);
//                }
//                cur_str = "";
//                continue;
//            }
//            cur_str += data[i];
//        }
//
//        cout << "preorder size: " << preorder_vec.size() << endl;
//        for (int pr: preorder_vec) {
//            cout << pr << " ";
//        }
//        cout << endl;
//        cout << "inorder size: " << inorder_vec.size() << endl;
//        for (int io: inorder_vec) {
//            cout << io << " ";
//        }
//        cout << endl;
//
//        return construct_tree_from_preorder_and_inorder(0, 0, int(inorder_vec.size() - 1), preorder_vec, inorder_vec);
//    }
//
//    void preorder_tree(TreeNode *root, string &preorder_str) {
//        if (root == nullptr) {
////            return;
////        }
////
////        preorder_str += to_string(root->val) + '#';
////        preorder_tree(root->left, preorder_str);
////        preorder_tree(root->right, preorder_str);
////    }
////
////    void inorder_tree(TreeNode *root, string &inorder_str) {
////        if (root == nullptr) {
////            return;
////        }
////
//        inorder_tree(root->left, inorder_str);
//        inorder_str += to_string(root->val) + '#';
//        inorder_tree(root->right, inorder_str);
//    }
//
//    TreeNode *construct_tree_from_preorder_and_inorder(int preStart, int inStart, int inEnd, vector<int> &preorder_vec,
//                                                       vector<int> &inorder_vec) {
//        if (preStart >= preorder_vec.size() || inStart > inEnd) {
//            return nullptr;
//        }
//
//        TreeNode *root = new TreeNode(preorder_vec[preStart]);
//        int index = 0;
//        for (int i = inStart; i <= inEnd; i++) {
//            if (preorder_vec[preStart] == inorder_vec[i]) {
//                index = i;
//                break;
//            }
//        }
//
//        root->left = construct_tree_from_preorder_and_inorder(preStart + 1, inStart, index - 1, preorder_vec,
//                                                              inorder_vec);
//        root->right = construct_tree_from_preorder_and_inorder(preStart + index - inStart + 1, index + 1, inEnd,
//                                                               preorder_vec, inorder_vec);
//        return root;
//    }
//};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root) {
        if (root == nullptr) {
            return nullptr;
        }

        string res = inorder(root, "");
        cout << res << endl;
        return res;
    }

    string inorder(TreeNode *root, string inorder_res) {
        if (root == nullptr) {
            inorder_res += "null,";
        } else {
            inorder_res += to_string(root->val) + ",";
            inorder_res = inorder(root->left, inorder_res);
            inorder_res = inorder(root->right, inorder_res);
        }

        return inorder_res;
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data) {
        string delim = ",";
        vector<string> data_v = stringSplit(data, delim);

        for (string v: data_v) {
            cout << v << " ";
        }
        cout << endl;

        auto root = rdeserialize(data_v);
        return root;
    }

    TreeNode *rdeserialize(vector<string> data_v) {
        if (data_v.size() == 0){
            return NULL;
        }

        if (data_v[0] == "null") {
            data_v.erase(data_v.begin());
            return NULL;
        }

        auto root = new TreeNode(stoi(data_v[0]));
        cout << root->val << endl;
        data_v.erase(data_v.begin());
        root->left = rdeserialize(data_v);
        root->right = rdeserialize(data_v);
        return root;
    }

    vector<string> stringSplit(const string &str, const string &delim) {
        vector<string> res;
        if (str.empty()) { return res; }

        // c_str 把string转换成c中的字符格式
        char *strs = new char[str.length() + 1];
        strcpy(strs, str.c_str());

        char *d = new char[delim.length() + 1];
        strcpy(d, delim.c_str());

        // 将字符串str分解成若干个单词，单词之间以delimiters字符串中的任一一个字符分割
        // 第一次调用strtok时, str应该是一个c风格的字符串（c-string）,随后的调用中, str应该是一个NULL指针
        char *p = strtok(strs, d);
        while (p) {
            string s = p;
            res.push_back(s);
            p = strtok(nullptr, d);
        }

        return res;
    }
};

int main() {
    // Your Codec object will be instantiated and called as such:
    // Codec codec;
    // codec.deserialize(codec.serialize(root));
    auto *l11 = new TreeNode(1);
    auto *l12 = new TreeNode(2);
    auto *l13 = new TreeNode(3);
    auto *l14 = new TreeNode(4);
    auto *l15 = new TreeNode(5);

    l11->left = l12;
    l11->right = l13;
    l12->left = l14;
    l12->right = l15;
    PrintTree(l11);

    Codec codec;
    auto res = codec.deserialize(codec.serialize(l11));
    PrintTree(res);
}
