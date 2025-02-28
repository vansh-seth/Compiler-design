#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define MAX_SIZE 100
int stack[MAX_SIZE];
int top = -1;
void push(int item) {
    if (top >= MAX_SIZE - 1) {
        printf("Stack Overflow\n");
        return;
    }
    top++;
    stack[top] = item;
}
int pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        return -1;
    }
    int item = stack[top];
    top--;
    return item;
}
int is_operator(char symbol) {
    if (symbol == '+' || symbol == '-' || symbol == '*' || symbol == '/') {
        return 1;
    }
    return 0;
}
int evaluate(char* expression) {
    int i = 0;
    char symbol = expression[i];
    int operand1, operand2, result;
    int num; 
    while (symbol != '\0') {
        if (isdigit(symbol)) {
            num = 0;
            while (isdigit(symbol)) {
                num = num * 10 + (symbol - '0');
                i++;
                symbol = expression[i];
            }
            push(num);
        }
        else if (is_operator(symbol)) { 
            operand2 = pop();
            operand1 = pop();
            switch(symbol) {
                case '+': result = operand1 + operand2; break;
                case '-': result = operand1 - operand2; break;
                case '*': result = operand1 * operand2; break;
                case '/': result = operand1 / operand2; break;
            }
            push(result);
            i++;  
            symbol = expression[i];
        }
        else {
            i++;  
            symbol = expression[i];
        }
    }
    result = pop();  
    return result;
}
int main() {
    char expression[MAX_SIZE];
    printf("Enter the postfix expression: ");
    scanf("%[^\n]%*c", expression);  
    int result = evaluate(expression);  
    printf("Result = %d\n", result);  
    return 0;
}
