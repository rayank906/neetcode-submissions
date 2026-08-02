class MinStack {
private:
    vector<int> stack;
    vector<int> min;
public:
    MinStack() {
        //ctor
    }
    
    void push(int val) {
        stack.push_back(val);
        if (stack.size() == 1) {
            min.push_back(val);
        }
        else {
            if (val < min[min.size() - 1]) {
                min.push_back(val);
            }
            else {
                min.push_back(min[min.size() - 1]);
            }
        }
    }
    
    void pop() {
        if (stack.size() == 0) { return; }
        stack.pop_back();
        min.pop_back();
    }
    
    int top() {
        return stack[stack.size() - 1];
    }
    
    int getMin() {
        return min[min.size() - 1];
    }
};
