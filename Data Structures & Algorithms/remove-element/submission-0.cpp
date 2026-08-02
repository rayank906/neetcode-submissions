class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] != val) {
                nums[l++] = nums[r];
            }
        }
        
        return l;
    }
};

/*
    1. make a left/right pointer to the first element
    2. right finds next element != val
    3. if first = val, reassign, else reassign next to that
    4. move left forward and keep looping
    5. return left
*/