// Created by Eric on 2020/3/5.

#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution {
public:

    // 解决不了3[a]2[b4[F]c]问题
//    string decodeString(string s) {
//
//        stack<string> ts;
//        stack<string> num;
//
//        string result;
//
//        string temp_num;
//        string temp_s;
//        // 将num数字单独提取出来
//        for (int i = 0; i < s.length(); i++) {
//            if (isdigit(s[i])) {
//                temp_num += s[i];
//                continue;
//            }
//            if (s[i] == '[') {
//                num.push(temp_num);
//                temp_num = "";
//            }
//            temp_s += s[i];
//        }
//
//        string temp_str;
//        for (int i = temp_s.length() - 1; i >= 0; i--){
//            if (temp_s[i] == ']'){
//                ts.push(to_string(temp_s[i]));
//                continue;
//            }
//            if (ts.size() == 1){
//                result = temp_s[i] + result;
//                continue;
//            }
//
//            if (temp_s[i] == '['){
//                ts.pop();
//                int cur_num = stoi(num.top()); num.pop();
//
////                cout << "before: " << temp_str << endl;
//                string cur_str = temp_str;
//                for (int k = 0; k < cur_num - 1; k++){
//                    temp_str += cur_str;
//                }
////                cout << "after:" << temp_str << endl;
//
//                if(ts.empty() && temp_str.size() != 0){
////                    cout << temp_str << endl;
//                    result = temp_str + result;
//                    temp_str = "";
//                }
//                continue;
//            }
//
//            if (ts.empty()){
//                result = temp_s[i] + result;
//                continue;
//            }
//
//            temp_str = temp_s[i] + temp_str;
//
//        }
//
////        cout << result << endl;
//        return result;
//
//    }

    string decodeString(string s) {
        stack<map<string, int>> temp;
        int multi = 0;
        string res;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '[') {
                map<string, int> res_multi;
                res_multi.insert(pair<string, int>(res, multi));
                temp.push(res_multi);
                res = "", multi = 0;
            } else if (s[i] == ']') {
                map<string, int> last_res_multi = temp.top(); temp.pop();
                string last_res = last_res_multi.begin()->first;
                int cur_multi = last_res_multi.begin()->second;

                string temp_res;
                for (int k = 0; k < cur_multi; k++) {
                    temp_res += res;
                }
                res = last_res + temp_res;
//                cout << "last_res: " << last_res << endl;
//                cout << "temp_res: " << temp_res << endl;

            } else if ('0' <= s[i] && s[i] <= '9') {
//                cout << c << endl;
//                cout << to_string(c) << endl;
                multi = multi * 10 + (s[i] - '0');
//                cout << multi << endl;
            } else {
                res += s[i];
            }
        }

        return res;
    }

};

int main() {
    string s = "3[a]2[b4[F]c]";
    Solution solution;
    string result = solution.decodeString(s);
    cout << result << endl;
}