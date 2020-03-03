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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode *temphead = head;
        while (temphead) {
            temphead = temphead->next;
            count += 1;
        }
        if (count == n){
            return head->next;
        }

        int front_n = count - n + 1;
        int front_count = 0;
        ListNode *result = head;
        ListNode *prev = NULL;
        ListNode *next = NULL;
        while(head){
            next = head->next;
            front_count = front_count + 1;
            if (front_count == front_n){
                prev->next = next;
                return result;
            }

            prev = head;
            head = head->next;
        }
        return NULL;
    }
};

int main(){
    ListNode *l1_1 = new ListNode(1);
//    ListNode *l1_2 = new ListNode(0);
//    ListNode *l1_3 = new ListNode(5);
//    l1_1->next = l1_2;
//    l1_2->next = l1_3;
    ListNode *l1 = l1_1;
    PrintListNode(l1);

    Solution solution;
    ListNode *result = solution.removeNthFromEnd(l1, 1);
    PrintListNode(result);
}