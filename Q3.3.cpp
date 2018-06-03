#include <stack>
#include <vector>
using namespace std;

class SetOfStacks {
    int threshold;
    vector<stack<int>> vecOfStacks;
    int currentStack;
    SetOfStacks(int threshold) {
        this.threshold = threshold;
        stack<int> defaultStack;
        this.vecOfStacks.push(defaultStack);
        this.currentStack = 0;
    }

    void push(int item) {
        if (vecOfStacks[currentStack].size() == threshold) {
            stack<int> newStack;
            newStack.push(item);
            
            vecOfStacks.push(newStack);
            currentStack++;
        } else {
            vecOfStacks[currentStack].push(item);
        }

    }

    int pop() {
        return 0;
    }
}