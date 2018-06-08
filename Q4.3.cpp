#include <vector>
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node * left;
    Node * right;
    Node * next;
};

void preOrderAdd(vector<Node *>& ll, Node * node, int depth) {
    if (node == NULL) return;

    if (ll.size() <= depth) {
        ll.push_back(node);
    }
    else {
        Node * temp = ll[depth];
        node->next = temp;
        ll[depth] = node;
    }
    preOrderAdd(ll, node->left, depth + 1);
    preOrderAdd(ll, node->right, depth + 1);
}

int main () {
    /**
     *        0
     *      1
     *    2   3
     *          4
    */
    Node node4 = { 4, NULL, NULL, NULL };
    Node node3 = { 3, NULL, &node4, NULL };
    Node node2 = { 2, NULL, NULL, NULL };
    Node node1 = { 1, &node2, &node3, NULL };
    Node node0 = { 0, &node1, NULL, NULL };

    vector<Node *> ll;
    preOrderAdd(ll, &node0, 0);
    for (vector<Node *>::iterator it = ll.begin(); it != ll.end(); ++it) {
        Node *node = *it;
        while(node != NULL) {
            cout << node->data << " "; 
            node = node->next;
        }
        cout << endl;
    }
}