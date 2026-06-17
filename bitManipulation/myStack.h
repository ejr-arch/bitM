#define MAX 100 //number of max items stack can accomodate

typedef struct{
	int items[MAX];
	int top;	
}Stack;

typedef enum{
	FALSE,
	TRUE
}boolean;

void init(Stack *S);

boolean isEmpty(Stack *S);

void push(Stack *S, int value);

void peek(Stack *S);

int pop(Stack *S);
