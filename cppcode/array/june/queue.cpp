#include "stdio.h"
#include "stdlib.h"

struct qNode{
    int data;
    struct qNode *next;
};

typedef struct qNode qNode;
typedef struct {
    qNode *q;
    int size;
    qNode* front;
    qNode* rear;
} Queue;


int queueIsEmpty(Queue *q) {
    if (q->front == NULL && q->rear == NULL) {
        printf("\nQUEUE is EMPTY\n");
        return 1;
    }
    return 0;
}

int queueTop(Queue *q) {
    if (queueIsEmpty(q)) {
        return -1;
    }
    return (q->front)->data;
}

int deque(Queue *q) {

}
void queuePush(Queue *q, int val) {

}
Queue *queueCreate(int maxSize) {
    Queue *q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = -1;
    q->size = maxSize;
    q->q = (int*)malloc(sizeof(int)*maxSize);
    return q;
}


int main(){

}