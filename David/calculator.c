#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long x = get_long("What is x? ");
    long y = get_long("What is y? ");

    printf("%li\n", x + y);
};