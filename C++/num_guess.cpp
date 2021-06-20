#include <iostream>
#include <time.h>
using namespace std;
//declarations
#define MAX_LEN 3 // sets max number of chartes in the input to two
char input[MAX_LEN];
//input function
void inputFunc() {
    cout << "Enter your guess! ";
    cin.getline (input, MAX_LEN);
}
//main function
int main() {
    //game explanation
    cout << "Guess a number between One and One Hundred!\nGood luck!\n";
    //declrations
    int intInput;
    //generates the random number
    srand(time(NULL));
    int random = rand()%101;
    //input
    inputFunc();
    //processes input
    while (random > 0){
        intInput = stoi(input);
        if (intInput == random) {
            cout << "You have entered the correct number!\n";
            break;
        } else if (intInput > random){
            cout << "You have entered a number that is too high!\n";
            inputFunc();
        } else if (intInput < random){
            cout << "You have entered a number that is too low!\n";
            inputFunc();
        }
}
return 0;
}
