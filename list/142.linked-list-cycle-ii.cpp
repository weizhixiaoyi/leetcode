// Created by Eric on 2020/3/3.

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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL){
            return NULL;
        }

        ListNode *slow = head;
        ListNode *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                break;
            }
        }
        if (slow != fast){
            return NULL;
        }
        fast = head;
        while (slow != fast){
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};

int main() {
    ListNode *l1_1 = new ListNode(3);
    ListNode *l1_2 = new ListNode(2);
    ListNode *l1_3 = new ListNode(0);
    ListNode *l1_4 = new ListNode(-4);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    l1_3->next = l1_4;
    l1_4->next = l1_2;
    ListNode *l1 = l1_1;

    Solution solution;
    ListNode *result = solution.detectCycle(l1);
    PrintListNode(result);
}
