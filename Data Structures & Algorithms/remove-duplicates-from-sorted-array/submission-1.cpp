class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int current_num = 0;
        int while_i = 0;

        // override all duplicates
        for (int i = 0; i < nums.size(); i=while_i) {
            current_num = nums[i];
            while_i = ++i;
            while (nums[while_i] == current_num) {
                nums[while_i] = -101;
                while_i++;
            }
        }

        // make an array with non zero values
        vector<int> array_2;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != -101) {
                array_2.push_back(nums[i]);
            }
        }

        nums = array_2;
        return nums.size();
    }
};

//PSEUDO
/*
    1. for every elem, replace all dupli w 0
    2. make a second array, add in all non zero elements from nums
    3. assign nums to array 2
    4. return nums.size
*/