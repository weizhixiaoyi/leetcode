// Created by Eric on 2020/3/4.

#include <iostream>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        if (s.length() %2 != 0){
            return false;
        }
        stack<char> front;
        stack<char> tail;

        for (char i: s){
            front.push(i);
        }

        while (!front.empty()){
            if (tail.empty()) {
                char temp = front.top();
                tail.push(temp);
                front.pop();
            }
            char cur_front = front.top();
            char cur_tail = tail.top();
            if ((cur_front == '[' && cur_tail == ']') || (cur_front == '{' && cur_tail == '}') ||
                (cur_front == '(' && cur_tail == ')')) {
//                cout << cur_front << " " << cur_tail << endl;
                front.pop();
                tail.pop();
            } else {
                front.pop();
                tail.push(cur_front);
            }
        }
        return tail.empty();
    }
};

int main() {
    string s = "(]";
    Solution solution;
    bool result = solution.isValid(s);
    cout << result << endl;
}