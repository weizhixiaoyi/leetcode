// Created by Eric on 2020/3/19.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// HINT
// G[n]表示总共的个数，F(i, n)表示n个数中，以i为节点,[1,..., i-1]为左子树, [i+1, ..., n-i]为右子树。
// G[n] = \sum_{i=1}^{n} F(i,n)
// F(i, n) = G[i - 1] * G[n - i]
// G[n] = \sum_{i=1}^{n}(G[i - 1] * G[n - i])

// 错误误区，开始解题时是从低往高进行推到，试图从数学上进行解答。
// 但实际没有理解清楚二叉搜索树的定义，没有考虑到G[n] = F(i,n)层次。想题目还是需要多从递归方面考虑。

class Solution {
public:
    int numTrees(int n) {
        vector<int> G(n);
        G[0] = 1;
        G[1] = 1;

        for (int i = 2; i <= n; i++) {
            for(int j = 1; j <= i; j++) {
                G[i] += G[j - 1] * G[i - j];
            }
        }

        return G[n];
    }
};

int main() {
    int n = 5;
    Solution solution;
    int res = solution.numTrees(n);
    cout << res << endl;
}