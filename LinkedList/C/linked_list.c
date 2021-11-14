#include <stdio.h>
#include <stdlib.h>

typedef struct registry {
    int content;
    struct registry *next;
} NODE;

void add(NODE *ll, int value){
    // time complexity: O(n) where n is the linked list height
    if (ll->next == NULL){
        NODE *new_node;
        new_node = malloc(sizeof(NODE));
        new_node->content = value;
        new_node->next = NULL;

        ll->next = new_node;
        return;
    }

    add(ll->next, value);
}

void recursivePrint(NODE *ll){
    if (ll != NULL){
        printf("%d\n", ll->content);
        recursivePrint(ll->next);
    }
};

int main(){

    NODE *ll = NULL;
    ll = malloc(sizeof(NODE));

    ll->content = 0;
    ll->next = NULL;

    add(ll, 1);

    return 0;
};
