// Created by Eric on 2020/3/4.

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
//    vector<int> dailyTemperatures(vector<int> &T) {
//        vector<int> front = T;
//        vector<int> tail;
//
//        vector<int> result;
//        int temp = front.back();
//        int max_t = temp;
//        front.pop_back();
//        tail.push_back(temp);
//        result.push_back(0);
//
//
//        while (!front.empty()) {
//            int cur_val = front.back();
//            int count = 0;
//            if (max_t <= cur_val){
//                count = 0;
//            } else {
//                for (int i : tail) {
//                    count = count + 1;
//                    if (i > cur_val) {
//                        break;
//                    }
//                }
//            }
//
//            if (cur_val > max_t){
//                max_t = cur_val;
//            }
//            front.pop_back();
//            tail.insert(tail.begin(), cur_val);
//            result.push_back(count);
//        }
//        reverse(result.begin(), result.end());
//        return result;
//    }
    vector<int> dailyTemperatures(vector<int> &T) {
        stack<int> sub;
        vector<int> result(T.size(), 0);

        for(int i = 0; i < T.size(); i++){
            while(!sub.empty() && T[i] > T[sub.top()]){
                int cur = sub.top(); sub.pop();
                result[cur] = i - cur;
            }
            sub.push(i);
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> daily = {73, 74, 75, 71, 69, 72, 76, 73};
    vector<int> result = solution.dailyTemperatures(daily);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
}
