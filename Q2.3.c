#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *next;
};

void deleteMiddle(struct node * middle) {
    while (middle->next->next != NULL) {
        middle->data = middle->next->data;
        middle = middle->next;
    }

    // Currently at second last element
    middle->data = middle->next->data;
    free(middle->next);
    middle->next = NULL;
    return;
}

void printElements(struct node * nod) {
    while (nod != NULL) {
        printf("Curr: %d\n", nod->data);
        nod = nod->next;
    }
    return;
}

int main( ) {
    struct node *node_1 = (struct node *) malloc(sizeof (struct node));
    struct node *node_2 = (struct node *) malloc(sizeof(struct node));
    struct node *node_3 = (struct node *) malloc(sizeof(struct node));
    struct node *node_4 = (struct node *) malloc(sizeof(struct node));
    struct node *node_5 = (struct node *) malloc(sizeof(struct node));

    node_5->next = NULL;
    node_5->data = 5;
    node_4->next = node_5;
    node_4->data = 4;
    node_3->next = node_4;
    node_3->data = 3;
    node_2->next = node_3;
    node_2->data = 2;
    node_1->next = node_2;
    node_1->data = 1;

    printElements(node_1);
    deleteMiddle(node_3);
    printElements(node_1);

    return 0;
}