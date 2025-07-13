#include <stdlib.h>
#include <stdio.h>

int main() {
    
    int secret = rand() % 10 + 1;
    int tries = 0;
    int guess;
    int score = 0;
    
    printf("Please enter your guess 1-10:\n");
    scanf("%d", &guess);
    
    while (guess != secret) {
        printf("Wrong! Try again\n");
        scanf("%d", &guess); 
        score++;
    }    
    printf("You got it in %d tries!\n", score);
    return 0;
}
