<<<<<<< HEAD:problem1.c
//Sum of all the multiples of 3 or 5 below a certain number.
=======

>>>>>>> 70f34d7dc9d7df7c47f7e7bd3600e8654fd89e98:3or5.c

#include <stdio.h>
#include <stdlib.h>

<<<<<<< HEAD:problem1.c
=======
//Find the sum of all the multiples of 3 or 5 below a certain number. (specific example from Project Euler)


>>>>>>> 70f34d7dc9d7df7c47f7e7bd3600e8654fd89e98:3or5.c
int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Proper usage: ./3or5 number");
    }

    int cutoff = atoi(argv[1]);
    int sum = 0;
    int threemultiples = (cutoff - 1) / 3;
    int fivemultiples = (cutoff - 1) / 5;
    do
    {
        sum = sum + (3 * threemultiples);
        threemultiples--;
    }
    while(threemultiples > 0);
    do
    {
        sum = sum + (5 * fivemultiples);
        fivemultiples--;
    }
    while(fivemultiples > 0);
    int sum15 = 0;
    int fifteenmultiples = (cutoff - 1) / 15;
    do
    {
        sum15 = sum15 + (15 * fifteenmultiples);
        fifteenmultiples--;
    }
    while (fifteenmultiples > 0);
    sum = sum - sum15;
    printf("Sum: %i\n", sum);
}
