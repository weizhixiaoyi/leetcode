// Created by Eric on 2020/3/4.

// Hint
// 1.归并排序
// 2.利用dummyHead来合并两个序列

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
    ListNode *sortList(ListNode *head) {
        ListNode *temp = head;
        int n = 0;
        while (temp) {
            n = n + 1;
            temp = temp->next;
        }

        // dummyHead->next后节点值排序后可能会发生变化, 但通过dummyHead可以返回排序后的结果值
        ListNode *dummyHead = new ListNode(-1);
        dummyHead->next = head;
        ListNode *cur = nullptr, *left = nullptr, *right = nullptr;

        // 依次增加比较的长度, 复杂度O(logn)
        for (int step = 1; step < n; step = 2 * step) {
            cur = dummyHead->next;
            auto tail = dummyHead;
            while (cur) {
                left = cur;
//                cout << "left: "; PrintListNode(left);

                right = split(left, step);
//                cout << "right: "; PrintListNode(right);


                cur = split(right, step);
//                cout << "cur: "; PrintListNode(cur);
//                cout << "left1: "; PrintListNode(left);
//                cout << "right1: "; PrintListNode(right);

                tail->next = merge(left, right);
//                cout << "#####################" << endl;
                while (tail->next) {
                    tail = tail->next;
                }
            }
        }
        return dummyHead->next;
    }

    ListNode *split(ListNode *head, int n){
        ListNode *cur = head;
        ListNode *right;

        while (--n && cur) {
            cur = cur->next;
        }
        if (!cur) return nullptr;

        right = cur->next;
        // 目的是将数据进行阶段, 如[8->7->4->3], head变为8, 后半部分为[7->4->3].
        cur->next = nullptr;

        return right;
    }

    ListNode *merge(ListNode *left, ListNode *right){
//        cout << "left && right" << endl;
//        PrintListNode(left);
//        PrintListNode(right);
        ListNode dummyHead(-1);
        ListNode *cur = &dummyHead;

        while (left && right){
            if (left->val < right->val) {
                cur->next = left;
                cur = cur->next;
                left = left->next;
            } else {
                cur->next = right;
                cur = cur->next;
                right = right->next;
            }
        }

        cur->next = left ? left : right;
        return dummyHead.next;
    }
};

int main() {
    ListNode *l1_1 = new ListNode(8);
    ListNode *l1_2 = new ListNode(7);
    ListNode *l1_3 = new ListNode(6);
    ListNode *l1_4 = new ListNode(5);
    ListNode *l1_5 = new ListNode(4);
    ListNode *l1_6 = new ListNode(3);
    ListNode *l1_7 = new ListNode(2);
    ListNode *l1_8 = new ListNode(1);
    l1_1->next = l1_2;
    l1_2->next = l1_3;
    l1_3->next = l1_4;
    l1_4->next = l1_5;
    l1_5->next = l1_6;
    l1_6->next = l1_7;
    l1_7->next = l1_8;
    ListNode *l1 = l1_1;

    Solution solution;
    ListNode *result = solution.sortList(l1);
    PrintListNode(result);
}

