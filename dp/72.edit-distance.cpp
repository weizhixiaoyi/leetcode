// Created by Eric on 2020/5/12.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int w1_len = word1.length(), w2_len = word2.length();
        if (w1_len == 0 || w2_len == 0) return max(w1_len, w2_len);
        vector<vector<int>> dp(w1_len + 1, vector<int>(w2_len + 1, 0));
        for (int i = 1; i <= w1_len; i++){
            for (int j = 1; j <= w2_len; j++){

            }
        }
    }
};

int main(){
    string s1, s2;
    Solution solution;
    while(true){
        cin >> s1;
        cin >> s2;
        int res = solution.minDistance(s1, s2);
        cout << "res: " << res << endl;
    }
}


