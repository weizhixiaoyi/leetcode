// Created by Eric on 2020/3/2.

// 请判断一个链表是否为回文链表。
// eg.1
// 输入: 1->2
// 输出: false
// eg.2
// 输入: 1->2->2->1
// 输出: true

// HINT: 不可直接进行翻转列表，因为每次操作头指针，翻转后会打乱head的位置。然后便不能直接比较。
// 可以用快慢指针把列表分成两半，翻转后半部分，然后再进行比较。

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
    cout << endl;
}

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return true;
        }

        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
//        PrintListNode(slow);
//        PrintListNode(fast);

        // 翻转后半部分
        ListNode* pre = NULL;
        ListNode* next = NULL;
        while(slow){
            next = slow->next;
            slow->next = pre;

            pre = slow;
            slow = next;
        }
//        PrintListNode(pre);

        while(pre){
            if(pre->val != head->val){
                return false;
            }
            head = head->next;
            pre = pre->next;
        }
        return true;
    }
};

int main(){
    ListNode* l1_1 = new ListNode(1);
    ListNode* l1_2 = new ListNode(2);
    ListNode* l1_3 = new ListNode(2);
    ListNode* l1_4 = new ListNode(1);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    l1_3->next = l1_4;
    ListNode* l1 = l1_1;

    Solution solution;
    bool result = solution.isPalindrome(l1);
    cout << result << endl;

}