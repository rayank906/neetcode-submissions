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

        ListNode* sub = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;

        return sub;
    }
};

/*
    base case: reverse a single node list. return node;
    recursive step: take a reversed list and reverse it and the element;
    1. do reassignment on head->next and reversedList(head->next);
*/
