#include<stdio.h>
#include <stdlib.h>
int input;
int main()
{
    srand(time(NULL));
    int r = rand() % 101;
    guess(r);
    while (r >= 0){
        if (r > input){
        printf("You have guessed too low!\n");
        guess(r);
        } else if (r < input){
        printf("You have guessed too high!\n");
        guess(r);
        }else {
        printf("You have guessed correctly!\n");
        break;
        }
    }
    return 0;
}
int guess(r){
    printf("Enter your guess! ");
    scanf("%d", &input);
}