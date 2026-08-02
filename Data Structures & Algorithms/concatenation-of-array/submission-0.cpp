class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans = nums;
        for (int i = 0; i < nums.size(); i++) {
            ans.push_back(nums[i]);
        }
        return ans;
    }
};

/*
    1. create a vector ans and assign to nums to copy elements over
    2. loop through nums from 0 to n
    3. ans[i+n] = nums[i]
    4. return ans
*/