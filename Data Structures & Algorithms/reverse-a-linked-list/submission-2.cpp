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
        if (!head) { return head; }
        
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* temp;

        while (curr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
};

/*
    0. make a pointer to the head
    1. push every element of the list onto a stack
    2. loop from the back and assign every element to the list
    3. return the new list
*/
