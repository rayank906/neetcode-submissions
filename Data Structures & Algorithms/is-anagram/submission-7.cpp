class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (auto c : s) {
            if (s_map.find(c) != s_map.end()) {
                s_map[c]++;
            }
            else {
                s_map[c] = 1;
            }
        }

        for (auto c : t) {
            if (t_map.find(c) != t_map.end()) {
                t_map[c]++;
            }
            else {
                t_map[c] = 1;
            }
        }

        return (s_map == t_map);
    }
};
