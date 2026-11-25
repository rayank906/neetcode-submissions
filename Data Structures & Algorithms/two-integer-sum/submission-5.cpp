class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
            - loop thru elems
            - if complement in idxMap, return [compIdx, currIdx]
            - else add curr elem and curr idx to idxMap
        */

        unordered_map<int, int> idxMap;
        for (int i = 0; i < nums.size(); i++) {
            auto it = idxMap.find(target - nums[i]);
            if (it != idxMap.end()) {
                return {it->second, i};
            }
            else {
                idxMap[nums[i]] = i;
            }
        }
        return {0, 0};
    }
};
