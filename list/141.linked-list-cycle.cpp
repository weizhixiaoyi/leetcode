// Created by Eric on 2020/3/1.

// 给定一个链表，判断链表中是否有环。
// 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

// eg.1
// 输入：head = [3,2,0,-4], pos = 1
// 输出：true
// 解释：链表中有一个环，其尾部连接到第二个节点。
// eg.2
// 输入：head = [1], pos = -1
// 输出：false
// 解释：链表中没有环。


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
    bool hasCycle(ListNode *head) {
        ListNode* pointer1 = head;
        ListNode* pointer2 = head;

        while(pointer1 && pointer2){
            if(pointer1->next == NULL){
                return false;
            }
            pointer1 = pointer1->next;
            if(pointer2->next == NULL){
                return false;
            }
            pointer2 = pointer2->next;
            if(pointer2->next == NULL){
                return false;
            }
            pointer2 = pointer2->next;

            if(pointer1 == pointer2){
                return true;
            }
        }
        return false;
    }
};

int main(){
    ListNode* l1_1 = new ListNode(1);
    ListNode* l1_2 = new ListNode(2);
    ListNode* l1_3 = new ListNode(4);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    ListNode* l1 = l1_1;

    Solution solution;
    solution.hasCycle(l1);
}