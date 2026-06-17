#include<stdio.h>
#include "myStack.h"

	void init(Stack *S){
		S->top = -1;
	}

	boolean isEmpty(Stack *S){
		if (S->top == -1)return TRUE;
		else return FALSE;
	}

	void push(Stack *S, int value){
		if (S->top == MAX - 1){
			printf("Stack overflow");
			return;
		}
		S->items[++S->top] = value;
	}

	void peek(Stack *S){
		if (isEmpty(S)){
			printf("Empty Stack");
			return;
		}
		printf("%d\n",S->items[S->top]);
	}

	int pop(Stack *S){
		if (isEmpty(S)){
			printf("Empty Stack");
			return 1;
		}	
		return S->items[S->top--];
	}

