#include <iostream>
using namespace std;

struct Node {
    int data;
    struct Node *next;
};

int doTheyIntersect(struct Node * list1, struct Node * list2) {
    struct Node * list1ptr = list1;
    while (list1ptr->next != NULL) {
        list1ptr = list1ptr->next;
    }
    struct Node * list2ptr = list2;
    while (list2ptr->next != NULL) {
        list2ptr = list2ptr->next;
    }
    if(list1ptr != list2ptr) return -1;

    // Go through list1 and set all the 'next' variables to NULL
    list1ptr = list1;
    struct Node * prev = list1ptr;
    list1ptr = list1ptr->next;
    while (list1ptr != NULL) {
        prev->next = NULL;
        prev = list1ptr;
        list1ptr = list1ptr->next;
    }

    list2ptr = list2;
    while (list2ptr != NULL) {
        if (list2ptr->next == NULL) {
            return list2ptr->data;
        }
        list2ptr = list2ptr->next;
    }
}

int main () {
    
    struct Node nodeD = {5, NULL};
    struct Node nodeC= {4, &nodeD};
    struct Node nodeB = {3, &nodeC};
    struct Node nodeA = {2, &nodeB};

    struct Node nodeY = {1, &nodeC};

    cout << doTheyIntersect(&nodeA, &nodeY) << endl;
}