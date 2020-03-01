// Created by Eric on 2020/3/1.

// 找到两个单链表相交的起始节点。

#include <iostream>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL) {
            return NULL;
        }

        while (headA) {
            ListNode *temp = headB;
            while (temp) {
                if (headA == temp) {
                    return headA;
                }
                temp = temp->next;
            }
            if (headA->next != NULL){
                headA = headA->next;
            }
            if (headB->next != NULL) {
                headB = headB->next;
            }
        }
        return NULL;
    }
};

int main() {

}