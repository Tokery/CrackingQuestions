#include <iostream>
#include "node.h"
using namespace std;

bool isValid(Node* tree, int* min, int* max) {
    if (tree == NULL) {
        return true;
    }
    else if (min != NULL && tree->data < *min) {
        return false;
    }
    else if (max != NULL && tree->data > *max) {
        return false;
    }
    return isValid(tree->left, min, &tree->data) && isValid(tree->right, &tree->data, max);
}

int main() {
    /**
     *     7
     *   4   8
     * 1  10
    */
    Node node1 = {1, NULL, NULL};
    Node node10 = {10, NULL, NULL};
    Node node4 = {4, &node1, &node10};
    Node node8 = {8, NULL, NULL};
    Node node7 = {7, &node4, &node8};

    cout << isValid(&node7, NULL, NULL) << endl;
}