class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        /*
            - init res vec, global map of anagram to idx in res
            - for every elem
                - build freq vector
                - convert freq vector to string
                - check in global map for idx
                    - if not there, create new vector and add curr to it
                    - add vec to res vec
                    - else add curr to res[idx], add to map
            - return res
        */
        vector<vector<string>> res;
        unordered_map<string, int> angToIdx;
        for (auto s : strs) {
            vector<int> freq(26, 0);
            for (auto c : s) {
                freq[c - 'a']++;
            }
            string freqString;
            for (auto i : freq) {
                freqString += to_string(i) += ",";
            }
            auto it = angToIdx.find(freqString);
            if (it != angToIdx.end()) {
                res[it->second].push_back(s);
            }
            else {
                vector<string> newVec {s};
                res.push_back(newVec);
                angToIdx[freqString] = res.size() - 1;
            }
        }
        return res;
    }
};
