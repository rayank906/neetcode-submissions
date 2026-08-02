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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) {
            if (!list2) {
                return nullptr;
            }
            return list2;
        }
        else {
            if (!list2) {
                return list1;
            }
        }

        ListNode* new_head;
        ListNode* return_list;

        if (list1->val < list2->val) {
            new_head = list1;
            list1 = list1->next;
        }
        else {
            new_head = list2;
            list2 = list2->next;
        }

        return_list = new_head;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                new_head->next = list1;
                list1 = list1->next;
            }
            else {
                new_head->next = list2;
                list2 = list2->next;
            }
            new_head = new_head->next;
        }

        if (list1) {
            new_head->next = list1;
        }
        if (list2) {
            new_head->next = list2;
        }

        return return_list;
    }
};

/*
    0. if any list is empty, return the non-empty or nullptr if both empty
    1. create a new head and a moving ptr, link it to the smaller list head
    2. while (both pointers are still valid), assign smaller value to new list
    3. update pointer accordingly
    4. if after the loop a ptr is still valid, append all the list to new list
    5. return new head
*/
