#include <stdio.h>

void sum_of_even()
{
    int sum_of_even = 0;
    for(int i=0;i<=100;i++)
    {
        if(i%2 == 0)
        {
            sum_of_even = sum_of_even + i;
        }
    }
    printf("Sum of even numbers: %d\n", sum_of_even);
}

void sum_of_odd()
{
    int sum_of_odd = 0;
    for(int i=0;i<=100;i++)
    {
        if(i%2 != 0)
        {
            sum_of_odd = sum_of_odd + i;
        }
    }
    printf("Sum of odd numbers: %d\n", sum_of_odd);
}

int fibonacci(int n)
{
    if(n == 0)
    {
        return 0;
    }
    else if (n == 1 || n == 2)
    {
        return 1;
    }
    else
    {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

int main()
{
    sum_of_even();
    sum_of_odd();
    int n = 20;
    int num = fibonacci(n);
    printf("Fibonacci of %d is %d\n", n, num);
}