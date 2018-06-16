//Sum of all even-valued terms less than 4 million

#include <stdio.h>

int main(void)
{
    int numone = 1;
    int numtwo = 2;
    int numthree = 0;
    int sum = 2;

    do
    {
        numthree = numone + numtwo;
        if (numthree % 2 == 0)
        {
            sum = sum + numthree;
        }
        numone = numtwo;
        numtwo = numthree;
    }
    while(numthree < 4000000);

    printf("Sum: %i\n", sum);
}
