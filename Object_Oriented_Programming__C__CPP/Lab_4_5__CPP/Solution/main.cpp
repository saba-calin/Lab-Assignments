#include <iostream>

#include "domain.h"
#include "vector.h"
#include "repository.h"
#include "admin_controller.h"
#include "user_controller.h"
#include "user_interface.h"
#include "tests.h"

// This is the main function of the program
int main()
{

    Tests tests = Tests();
    tests.RunAllTests();

    Repository repo;
    AdminController adminController(repo);
    UserController userController(repo);
    UserInterface ui = UserInterface(adminController, userController);
    ui.Run();

    return 0;
}
