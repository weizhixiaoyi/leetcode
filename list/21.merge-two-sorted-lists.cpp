// Created by Eric on 2020/3/1.

// 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4

#include <iostream>
#include <algorithm>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void PrintListNode(ListNode* l){
    while(l){
        cout << l->val << " ";
        l = l->next;
    }
}

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* merge = new ListNode(0);
        ListNode* merge1 = merge;
        while(l1 && l2){
            if(l1->val < l2->val){
                merge->next = new ListNode(l1->val);
                merge = merge->next;
                l1 = l1->next;
            }
            else{
                merge->next = new ListNode(l2->val);
                merge = merge->next;
                l2 = l2->next;
            }
        }
        if(l1 == NULL){
            merge->next = l2;
        }
        else{
            merge->next = l1;
        }
        ListNode* result = merge1->next;
        return result;
    }
};

int main(){
    ListNode* l1_1 = new ListNode(1);
    ListNode* l1_2 = new ListNode(2);
    ListNode* l1_3 = new ListNode(4);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    ListNode* l1 = l1_1;

    ListNode* l2_1 = new ListNode(1);
    ListNode* l2_2 = new ListNode(3);
    ListNode* l2_3 = new ListNode(4);
    l2_1->next = l2_2;
    l2_2->next = l2_3;
    ListNode* l2 = l2_1;

    PrintListNode(l1);
    cout << endl;
    PrintListNode(l2);
    cout << endl;

    Solution solution;
    ListNode* result = solution.mergeTwoLists(l1, l2);
    PrintListNode(result);
}