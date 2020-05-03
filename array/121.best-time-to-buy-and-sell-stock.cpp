// Created by Eric on 2020/5/3.
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // way1
//        int max_value = 0;
//        for(int i = 0; i < prices.size(); i++){
//            for(int j = i + 1; j < prices.size(); j++){
//                int cur_value = prices[j] - prices[i];
//                if(cur_value > max_value){
//                    max_value = cur_value;
//                }
//            }
//        }
//        return max_value;
        // way 2
        if (prices.size() == 0 || prices.size() == 1){
            return 0;
        }
        int min_value = prices[0], min_index = 0;
        int max_res = 0;
        for (int i = 0; i< prices.size(); i++){
            if (prices[i] < min_value){
                min_value = prices[i];
            }
            else if (prices[i] - min_value > max_res){
                max_res = prices[i] - min_value;
            }
        }
        return max_res;
    }
};

int main(){
    vector<int> v;
    for(int i = 0; i < 3; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    Solution solution;
    int res = solution.maxProfit(v);
    cout << res << endl;
}

