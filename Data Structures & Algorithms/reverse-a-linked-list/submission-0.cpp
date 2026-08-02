/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) { return head; }

        ListNode* temp = head;
        stack<int> list_stack;

        while (temp != nullptr) {
            list_stack.push(temp->val);
            temp = temp->next;
        }

        ListNode* temp_2 = head;
        while (temp_2 != nullptr) {
            temp_2->val = list_stack.top();
            list_stack.pop();
            temp_2 = temp_2->next;
        }

        return head;
    }
};

/*
    0. make a pointer to the head
    1. push every element of the list onto a stack
    2. loop from the back and assign every element to the list
    3. return the new list
*/
