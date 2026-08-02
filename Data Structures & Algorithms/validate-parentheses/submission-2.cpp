class Solution {
public:
    bool isValid(string s) {
        if (s.size() < 2) { return false; }
        vector<char> opening_brackets;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                opening_brackets.push_back(s[i]);
            }
            else {
                if (opening_brackets.size() == 0) {
                    return false;
                }
                else if (s[i] == ')') {
                    if (opening_brackets[opening_brackets.size() - 1] != '(') {
                        return false;
                    }
                    opening_brackets.pop_back();
                }
                else if (s[i] == ']') {
                    if (opening_brackets[opening_brackets.size() - 1] != '[') {
                        return false;
                    }
                    opening_brackets.pop_back();
                }
                else if (s[i] == '}') {
                    if (opening_brackets[opening_brackets.size() - 1] != '{') {
                        return false;
                    }
                    opening_brackets.pop_back();
                }
            }
        }
        if (opening_brackets.size() != 0) {
            return false;
        }
        return true;
    }
};

/*
    1. make a vector and push back encountered opening brackets
    2. if closing bracket encountered, check top of the stack for opening bracket
    3. if not found, return false
*/
