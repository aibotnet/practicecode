#include "stdio.h"
#include "stdlib.h"

typedef struct {
    int *q;
    int size;
    int front;
    int rear;
} Queue;
typedef struct {
    Queue *q1;
    Queue *q2;
} Stack;

int queueIsEmpty(Queue *q) {
    if (q->front == -1 && q->rear == -1) {
        printf("\nQUEUE is EMPTY\n");
        return 1;
    }
    return 0;
}
int queueIsFull(Queue *q) {
    if (q->rear == q->size-1) {
        return 1;
    }
    return 0;
}
int queueTop(Queue *q) {
    if (queueIsEmpty(q)) {
        return -1;
    }
    return q->q[q->front];
}
int queuePop(Queue *q) {
    if (queueIsEmpty(q)) {
        return -1;
    }
    int item = q->q[q->front];
    if (q->front == q->rear) {
        q->front = q->rear = -1;
    }
    else {
        q->front++;
    }
    return item;
}
void queuePush(Queue *q, int val) {
    if (queueIsFull(q)) {
        printf("\nQUEUE is FULL\n");
        return;
    }
    if (queueIsEmpty(q)) {
        q->front++;
        q->rear++;
    } else {
        q->rear++;
    }
    q->q[q->rear] = val;
}
Queue *queueCreate(int maxSize) {
    Queue *q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = -1;
    q->size = maxSize;
    q->q = (int*)malloc(sizeof(int)*maxSize);
    return q;
}
/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
    Stack **s = (Stack**) stack;
    *s = (Stack*)malloc(sizeof(Stack));
    (*s)->q1 = queueCreate(maxSize);
    (*s)->q2 = queueCreate(maxSize);
}

/* Push element x onto stack */
void stackPush(Stack *stack, int element) {
    Stack **s = (Stack**) stack;
    queuePush((*s)->q2, element);
    while (!queueIsEmpty((*s)->q1)) {
        int item = queuePop((*s)->q1);
        queuePush((*s)->q2, item);
    }
    Queue *tmp = (*s)->q1;
    (*s)->q1 = (*s)->q2;
    (*s)->q2 = tmp;
}

/* Removes the element on top of the stack */
void stackPop(Stack *stack) {
    Stack **s = (Stack**) stack;
    queuePop((*s)->q1);
}

/* Get the top element */
int stackTop(Stack *stack) {
    Stack **s = (Stack**) stack;
    if (!queueIsEmpty((*s)->q1)) {
      return queueTop((*s)->q1);
    }
    return -1;
}

/* Return whether the stack is empty */
bool stackEmpty(Stack *stack) {
    Stack **s = (Stack**) stack;
    if (queueIsEmpty((*s)->q1)) {
        return true;
    }
    return false;
}

/* Destroy the stack */
void stackDestroy(Stack *stack) {
    Stack **s = (Stack**) stack;
    free((*s)->q1);
    free((*s)->q2);
    free((*s));
}

int main()
{
  Stack *s = NULL;
  stackCreate((Stack*)&s, 10);
  stackPush((Stack*)&s, 44);
  //stackPop((Stack*)&s);
  printf("\n%d", stackTop((Stack*)&s));
  stackDestroy((Stack*)&s);
  return 0;
}