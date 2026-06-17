#include<stdio.h>

int bitLength(int number){
	int count = 0;
	while(number > 0){
		number = number >> 1;
		count++;
	}
	return count;
}

void toBinary(int number){
	if (number < 0){
		unsigned int bit = (unsigned int)number;
		for(int i = 31; i >=0; i--){
			printf("%d",(number >> i) & 1);
		}
	}
	else if(number ==0 )printf("0");
	else{
	for(int i = bitLength(number) - 1; i >= 0; i--){
		printf("%d ",(number >> i) & 1);
	}
	}
}

int main(int argc, char* argv[]){
	int number;
	printf("Enter number: ");
	scanf("%d", &number);
	toBinary(number);
}
