// Created by Eric on 2020/3/4.

#include <iostream>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

void PrintListNode(ListNode *l) {
    while (l) {
        cout << l->val << " ";
        l = l->next;
    }
    cout << endl;
}

class Solution {
public:
    ListNode* sortList(ListNode* head) {

    }
};

int main(){
    ListNode *l1_1 = new ListNode(3);
    ListNode *l1_2 = new ListNode(2);
    ListNode *l1_3 = new ListNode(1);
    ListNode *l1_4 = new ListNode(3);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    l1_3->next = l1_4;
    ListNode *l1 = l1_1;

    Solution solution;
    ListNode *result = solution.sortList(l1);
    PrintListNode(result);
}

