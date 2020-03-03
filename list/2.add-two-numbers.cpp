// Created by Eric on 2020/3/2.

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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        if (l1->next == NULL && l1->val == 0) {
            return l2;
        }
        if (l2->next == NULL && l2->val == 0) {
            return l1;
        }

        ListNode *temp = new ListNode(NULL);
        ListNode *result = temp;

        int carry = 0;
        while (l1 && l2) {
            int l1_val = l1->val;
            int l2_val = l2->val;
            l1 = l1->next;
            l2 = l2->next;
            int cur_val = l1_val + l2_val;

            if (carry == 1) {
                cur_val = cur_val + 1;
                carry = 0;
            }
            if (cur_val >= 10) {
                carry = 1;
                cur_val = cur_val - 10;
            }

            ListNode *cur_node = new ListNode(cur_val);
            temp->next = cur_node;
            temp = temp->next;
        }
        while (l1) {
            int cur_val = l1->val;
            l1 = l1->next;
            if (carry == 1) {
                cur_val = cur_val + 1;
                carry = 0;
            }
            if (cur_val >= 10) {
                carry = 1;
                cur_val = cur_val - 10;
            }
            ListNode *cur_node = new ListNode(cur_val);
            temp->next = cur_node;
            temp = temp->next;
        }
        while (l2) {
            int cur_val = l2->val;
            l2 = l2->next;
            if (carry == 1) {
                cur_val = cur_val + 1;
                carry = 0;
            }
            if (cur_val >= 10) {
                carry = 1;
                cur_val = cur_val - 10;
            }
            ListNode *cur_node = new ListNode(cur_val);
            temp->next = cur_node;
            temp = temp->next;
        }
        if (carry == 1){
            ListNode *cur_node = new ListNode(1);
            temp->next = cur_node;
            temp = temp->next;
        }

        result = result->next;
        return result;
    }
};

int main() {
    ListNode *l1_1 = new ListNode(1);
//    ListNode *l1_2 = new ListNode(0);
//    ListNode *l1_3 = new ListNode(5);
//    l1_1->next = l1_2;
//    l1_2->next = l1_3;
    ListNode *l1 = l1_1;

    ListNode *l2_1 = new ListNode(9);
    ListNode *l2_2 = new ListNode(9);
//    ListNode *l2_3 = new ListNode(5);
    l2_1->next = l2_2;
//    l2_2->next = l2_3;
    ListNode *l2 = l2_1;

    PrintListNode(l1);
    PrintListNode(l2);

    Solution solution;
    ListNode *result = solution.addTwoNumbers(l1, l2);
    PrintListNode(result);
}