// Created by Eric on 2020/3/3.

#include <iostream>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    int min;
    Node *next;

    Node(int val, int min): val(val), min(min), next(NULL) {}
    Node(int val, int min, Node *next):val(val), min{min}, next(next){}
};

class MinStack {
public:
    /** initialize your data structure here. */
    // 构造函数
    Node *head = nullptr;
    MinStack() {

    }

    void push(int x) {
        if (head == nullptr){
            head = new Node(x, x);
        }
        else{
            head = new Node(x, min(x, head->min), head);
        }
    }

    void pop() {
        head = head->next;
    }

    int top() {
        cout << head->val << endl;
        return head->val;
    }

    int getMin() {
        cout << head->min << endl;
        return head->min;
    }
};


int main() {
    MinStack minStack;
    minStack.push(2);
    minStack.push(0);
    minStack.push(3);
    minStack.push(0);
    minStack.getMin();
    minStack.pop();
    minStack.getMin();
    minStack.pop();
    minStack.getMin();
    minStack.pop();
    minStack.getMin();
}
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */