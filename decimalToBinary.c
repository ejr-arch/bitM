#include "myStack.h"
#include<stdio.h>


void binaryString(Stack *stack, int number){
	if (number < 0){
		printf("number can't be negative");
		return ;
	}
	if ((number/2) == 0){
		push(stack, number);
		return;
	}
	push(stack, (number % 2));
	binaryString(stack, number/2);
}

int main(int argc, char* argv[]){
	int number;
	printf("Enter number to convert: ");
	scanf("%d",&number);
	
	Stack stack;
	init(&stack);

	binaryString(&stack, number);
	
	while(!isEmpty(&stack)){
		printf("%d ",pop(&stack));
	}
}
