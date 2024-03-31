#include <stdio.h>
#include <math.h>
#include <stdbool.h>


struct Tuple
{
    int a, b;
};


// This function is used to print the menu of the program.
// @param: None
// @return: None
void PrintMenu()
{
    printf("\n");
    printf("Press 1 to read a vector of numbers from the console.\n");
    printf("Press 2 to test the first functionality.\n");
    printf("Press 3 to test the second functionality.\n");
    printf("Press 4 to close the program.\n");
}


// This function is used to check if a number is prime.
// @param n: An integer representing the number to be checked.
// @return: True if the number is prime, false otherwise.
bool IsPrime(int n)
{
    if (n <= 3)  return n >= 2;
    if (n % 2 == 0 || n % 3 == 0)  return false;
    for (int i = 5; i * i <= n; i += 6)
    {
        if (n % i == 0 || (n + 2) % i == 0)
        {
            return false;
        }
    }
    return true;
}


// This function is used to generate the first n prime numbers.
// @param n: An integer representing the number of prime numbers to be generated.
// @return: None
void GeneratePrimes(int n)
{
    int candidate = 2;
    while (n > 0)
    {
        if (IsPrime(candidate) == true)
        {
            printf("%d ", candidate);
            n--;
        }
        candidate++;
    }
}


// This function is used to compute the greatest common divisor of two numbers.
// @param a: An integer representing the first number.
// @param b: An integer representing the second number.
// @return: An integer representing the greatest common divisor of the two numbers.
int GCD(int a, int b)
{
    if (a == 0)  return b;
    if (b == 0)  return a;

    while (b != 0)
    {
        int c = a % b;
        a = b;
        b = c;
    }
    return a;
}


// This function is used to find the indices of the longest sequence of numbers in a vector
// such that the GCD of any two consecutive numbers is 1.
// @param v: The vector of numbers.
// @param len: The length of the vector.
// @return: A tuple containing the indices of the longest sequence, or (0, -1) if the vector does not contain any such sequence.
struct Tuple FindLongestSequence(int *v, int len)
{
    int cnt = 0, start = 0;
    int max = 0, left = 0, right = -1;
    for (int i = 0; i < len - 1; i++)
    {
        if (GCD(abs(v[i]), abs(v[i + 1])) == 1)
        {
            cnt += 1;
        }
        else
        {
            if (cnt > max)
            {
                max = cnt;
                left = start;
                right = i;
            }
            cnt = 0;
            start = i + 1;
        }
    }
    if (cnt > max)
    {
        left = start;
        right = len - 1;
    }

    struct Tuple t;
    t.a = left;
    t.b = right;
    return t;
}


// This function is used to print the length and the sequence between two indices of a vector.
// @param v: The vector of numbers.
// @param a: The left index.
// @param b: The right index.
// @return: None
void PrintSequence(int *v, int a, int b)
{
    printf("The length of the sequence is: %d\n", b - a + 1);
    for (int i = a; i <= b; i++)
    {
        printf("%d ", v[i]);
    }
}


// This is the main function of the program.
int main()
{
    int option = 0, len = 0, *v;
    while (option != 4)
    {
        PrintMenu();

        scanf("%d", &option);
        switch (option)
        {
            case 1:
                printf("len =");
                scanf("%d", &len);

                v = (int*) malloc(len * sizeof(int));
                for (int i = 0; i < len; i++)
                {
                    scanf("%d", &v[i]);
                }
                break;
            case 2:
                int n;
                printf("n =");
                scanf("%d", &n);

                GeneratePrimes(n);
                break;
            case 3:
                if (len <= 0)
                {
                    printf("The vector is empty!");
                    continue;
                }

                struct Tuple t = FindLongestSequence(v, len);
                PrintSequence(v, t.a, t.b);
                break;
            case 4:
                printf("Closing the program...");
                break;
            default:
                printf("Error: Invalid input!");
                break;
        }
    }

    return 0;
}