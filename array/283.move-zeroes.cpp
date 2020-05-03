// Created by Eric on 2020/5/3.
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//采用双指针思路，快指针正常行走，慢指针会指向0元素
class Solution{
public:
    void moveZeroes(vector<int> &nums){
        for (int i=0, j=0; i < nums.size(); i++){
            if(nums[i] != 0){
                swap(nums[i], nums[j]);
                j++;
            }
        }
    }
};

int main(){
    int nums[5] = {0,1,0,3,12};
    vector<int> a(nums, nums + 5);
    Solution solution;
    solution.moveZeroes(a);
}
