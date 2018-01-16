#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *next;
};

void printElements(struct node * nod) {
    while (nod != NULL) {
        printf("Curr: %d\n", nod->data);
        nod = nod->next;
    }
    return;
}

int getNumberFromList(struct node * nod, int factor) {
    if (nod == NULL) return 0;
    return nod->data * factor + getNumberFromList(nod->next, factor * 10);
}

int addLinkedLists(struct node * num_1, struct node * num_2) {
    int num1 = getNumberFromList(num_1, 1);
    int num2 = getNumberFromList(num_2, 1);
    return num1 + num2;
}

struct node * convertToList(int num) {
    
    // Extract last digit
    int current = num % 10;
    // Make final digit zero
    num = num - current; // 23 becomes 20    
    // Shorten entire number
    num = num / 10;
    struct node * ret = (struct node *) malloc(sizeof (struct node));
    ret->data = current;
    if (num == 0) {
        ret->next = NULL;
    }
    else {
        ret->next = convertToList(num);
    }
    return ret;
}

int main () {
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
    // node_1 represents the number 54321
    printf("number: %d\n", addLinkedLists(node_1, node_1));
    
    struct node * answer = convertToList(addLinkedLists(node_1, node_1));
    printElements(answer);
}