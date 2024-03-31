#include <stdio.h>

#include "user_interface.h"
#include "tests.h"

// This is the 'main' function of the program
// @param: none
// @return: none
int main()
{
    TestAll();

    UI ui = CreateUI();
    Start(&ui);

    return 0;
}
