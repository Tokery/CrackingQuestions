#include <queue>
#include <iostream>
#include <vector>
using namespace std;

struct Node {
    vector<Node *> neighbours;
    int data;
    bool marked;
};

bool isConnected(Node * node1, Node * node2) {
    queue<Node *> q;
    q.push(node1);
    node1->marked = true;
    while (!q.empty()) {
        Node * curr = q.front();
        q.pop();
        for (vector<Node *>::iterator it = curr->neighbours.begin(); it != curr->neighbours.end(); ++it) {
            if ((*it)->marked == false) {
                if ((*it) == node2) {
                    return true;
                }
                (*it)->marked = true;
                q.push(*it);
            }
        }
    }
    return false;
}


int main () {
    /**
     * node1 -> node3 -> node2
     *       \-> node4 
     */
    vector<Node *> node2neigh;
    Node node2 = { node2neigh, 2, false };
    vector<Node *> node4neigh;
    Node node4 = { node4neigh, 4, false };
    vector<Node *> node3neigh;
    node3neigh.push_back(&node2); // If removed should return false
    Node node3 = { node3neigh, 3, false };
    vector<Node *> node1neigh;
    node1neigh.push_back(&node3);
    node1neigh.push_back(&node4);
    Node node1 = { node1neigh, 1, false };
    
    cout << "Result " << isConnected(&node1, &node2) << endl;
}