// Created by Eric on 2020/3/1.

// 反转一个单链表。
// 输入: 1->2->3->4->5->NULL
// 输出: 5->4->3->2->1->NULL

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
}

class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }

        ListNode *pre = NULL;
        ListNode *next = NULL;

        while (head) {
            next = head->next;
            head->next = pre;

            pre = head;
            head = next;
        }
        return pre;
    }
};

int main() {
    ListNode *l1_1 = new ListNode(1);
    ListNode *l1_2 = new ListNode(2);
    ListNode *l1_3 = new ListNode(3);
    ListNode *l1_4 = new ListNode(4);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    l1_3->next = l1_4;
    ListNode *l1 = l1_1;

    ListNode* l2_1 = new ListNode(1);
    ListNode* l2_2 = new ListNode(3);
    ListNode* l2_3 = new ListNode(4);
    l2_1->next = l2_2;
    l2_2->next = l2_3;
    ListNode* l2 = l2_1;

    Solution solution;
    ListNode *result = solution.reverseList(l1);
    PrintListNode(result);
}