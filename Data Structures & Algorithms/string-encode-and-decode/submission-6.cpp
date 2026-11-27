class Solution {
public:

    string encode(vector<string>& strs) {
        /*
            - append len of str and ! to seperate
            - append str next to it
            - repeat for all strs    
        */
        string encoded;
        for (auto& s : strs) {
            encoded += to_string(s.size()) + "!" + s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        /*
            - build number until !
            - read number amt of chars
            - add to vector
        */
        int i = 0;
        string num = "";
        vector<string> res;
        while (i < s.size()) {
            if (s[i] != '!') {
                num += s[i];
                i++;
            }
            else {
                int lenStr = stoi(num);
                num = "";
                res.push_back(s.substr(i + 1, lenStr));
                i += (1 + lenStr);
            }
        }
        return res;
    }
};
