#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <queue>
using namespace std;

struct Node {
    Node (char data): data(data) {
        vector<Node *> temp;
        this->children = temp;
        this->seen = false;
        this->hasParent= false;
    }
    char data;
    bool hasParent;
    vector<Node *> children;
    bool seen;
};

void printBreadthFirst(Node * node) {
    queue<Node *> q;
    q.push(node);
    while(!q.empty()) {
        Node * curr = q.front();
        q.pop();
        for (auto it = curr->children.begin(); it != curr->children.end(); ++it) {
            if (!((*it)->seen)) {
                q.push(*it);
                (*it)-> seen = true;
            }
        }
        cout << curr->data << " ";
    }
}

void findBuildOrder(vector<char>& projects, vector<pair<char, char> >& deps) {
    unordered_map<char, Node *> rootNodes;
    // Create hash table of nodes
    for (vector<char>::iterator it = projects.begin(); it != projects.end(); ++it) {
        Node* temp = new Node (*it);
        rootNodes.insert( {{*it, temp }});
    }

    // Assign direct parent-child relationships where they exist
    for (auto it = deps.begin(); it != deps.end(); ++it) {
        char parentName = it->second;
        char childName = it->first;
        Node * parentNode = rootNodes[parentName];
        Node * childNode = rootNodes[childName];
        childNode->hasParent = true;
        parentNode->children.emplace_back(childNode);
    }
    // Iterate through hash table and print the dependency tree of any node with no parent
    for (auto it = rootNodes.begin(); it != rootNodes.end(); ++it) {
        if (it->second->hasParent) {
            continue;
        }
        printBreadthFirst(it->second);
    }

}

int main () {
    vector<char> projects = { 'a', 'b', 'c', 'd', 'e', 'f'};
    vector<pair<char, char> > deps = { 
        make_pair('d', 'a'), 
        make_pair('b', 'f'),
        make_pair('d', 'b'),
        make_pair('a', 'f'),
        make_pair('c', 'd')
    };
    findBuildOrder(projects, deps);
    return 0;
}