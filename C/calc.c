#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* calulator
*/
int main()
{
/* var declrations*/
int num1;
int num2;
int product;
char opp[1]="";
    /* user inputs*/
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the opperator you wish to use: ");
    scanf("%s", opp);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    /* caluclations*/
    if (strcmp(opp,"+")==0){
    printf("The answer is %d \n", num1 + num2);
    }
    else if (strcmp(opp,"-")==0){
    printf("The answer is %d \n", num1 - num2);
    }
    else if (strcmp(opp,"*")==0){
    printf("The answer is %d \n", num1 * num2);
    }
    else if (strcmp(opp,"/")==0){
    printf("The answer is %d \n", num1 / num2);
    }
    else{
    printf("You have entered an invalid opperator");
    }
    return 0;
}
