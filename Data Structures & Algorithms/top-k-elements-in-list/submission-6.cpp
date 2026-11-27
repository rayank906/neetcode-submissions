class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /*
            - init max heap
            - use a map to cnt
            - append elem, cnt to max heap
            - pop first k elements off the heap    
        */
        unordered_map<int, int> freqMap;
        priority_queue<pair<int, int>> maxHeap;
        for (auto& elem : nums) {
            if (freqMap.find(elem) != freqMap.end()) {
                freqMap[elem]++;
            }
            else {
                freqMap[elem] = 1;
            }
        }
        for (auto& [elem, count] : freqMap) {
            maxHeap.push({count, elem});
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            auto top = maxHeap.top();
            maxHeap.pop();
            res.push_back(top.second);
        }
        return res;
    }
};
