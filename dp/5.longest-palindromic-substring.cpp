// Created by Eric on 2020/5/12.

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

// dp
//class solution {
//public:
//    string longestpalindrome(string s) {
//        int s_len = s.length();
//        if (s_len == 0) return "";
//        vector<vector<int>> dp(s_len, vector<int>(s_len, 0));
//        for (int i = 0; i < s_len; i++) {
//            dp[i][i] = 1;
//            if (i < s_len - 1) {
//                if (s[i] == s[i + 1]) dp[i][i + 1] = 1;
//            }
//        }
//        int max_lens = 1;
//        int left = 0, right = 0;
//        for (int i = s_len - 2; i >= 0; i--) {
//            for (int j = i + 1; j < s_len; j++) {
//                if (j != i + 1) {
//                    if (dp[i + 1][j - 1] && s[i] == s[j]) {
//                        dp[i][j] = 1;
//                    }
//                }
//                if (dp[i][j] && max_lens < j - i + 1) {
////                    cout << i << " " << j << endl;
//                    max_lens = j - i + 1;
//                    left = i;
//                    right = j;
////                    cout << max_s << endl;
//                }
//            }
//        }
////        for (int i = 0; i < s_len; i++) {
////            for (int j = 0; j < s_len; j++) {
////                cout << dp[i][j] << " ";
////            }
////            cout << endl;
////        }
//        string max_s = s.substr(left, right - left + 1);
//        return max_s;
//    }
//};

class Solution {
public:
    string longestPalindrome(string s) {
        int s_len = s.length();
        if (s_len == 0) return "";
        int max_lens = 1;
        int left = 0, right = 0;
        for (int i = 0; i < s_len - 1; i++) {
//            cout << "i: " << i << endl;
            int len1 = expandString(s, i, i);
//            cout << "len1: " << len1 << endl;
            int len2 = expandString(s, i, i + 1);
//            cout << "len2: " << len2 << endl;
            int cur_len = max(len1, len2);
//            cout << "######" << endl;
            if (cur_len > max_lens) {
                max_lens = cur_len;
                left = i - int((cur_len  - 1)/ 2);
                right = i + int(cur_len / 2);
            }
        }
        cout << left << " " << right << endl;
        return s.substr(left, right - left + 1);
    }

    int expandString(string s, int L, int R) {
        // 取L和R中间元素
        while (L >= 0 && R < s.length() && s[L] == s[R]) {
            L = L - 1;
            R = R + 1;
        }
//        cout << "L: " << L << " R: " << R << endl;
        return R - L - 1;
    }
};

int main() {
    string s;
    Solution solution;
    while (true) {
        cin >> s;
        string res = solution.longestPalindrome(s);
        cout << "res: " << res << endl;
    }
}
