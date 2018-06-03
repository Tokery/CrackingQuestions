#include <stack>
#include <vector>
#include <iostream>
using namespace std;

class SetOfStacks {
    int threshold;
    vector< stack<int> > vecOfStacks;
    int currentStack;
    public:
        SetOfStacks(int threshold) {
            this->threshold = threshold;
            stack<int> defaultStack;
            this->vecOfStacks.push_back(defaultStack);
            this->currentStack = 0;
        }

        void push(int item) {
            if (vecOfStacks[currentStack].size() == threshold) {
                cout << "Adding new stack" << endl;
                stack<int> newStack;
                newStack.push(item);
                
                vecOfStacks.push_back(newStack);
                currentStack++;
            } else {
                vecOfStacks[currentStack].push(item);
            }

        }

        int pop() {
            int item = vecOfStacks[currentStack].top();
            vecOfStacks[currentStack].pop();
            if (vecOfStacks[currentStack].size() == 0) {
                cout << "Removing stack" << endl;
                vecOfStacks.pop_back();
                currentStack--;
            }
            return item;
        }
};

int main () {
    SetOfStacks sos (2);
    sos.push(1);
    sos.push(2);
    cout << "Done pushing 2" << endl;
    sos.push(3);
    sos.pop();
    return 0;
}