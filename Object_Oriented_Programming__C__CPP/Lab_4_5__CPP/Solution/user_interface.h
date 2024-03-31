#ifndef OOP_A4_5_916_SABAILA_CALIN_USER_INTERFACE_H
#define OOP_A4_5_916_SABAILA_CALIN_USER_INTERFACE_H

#include <cstring>

#include "admin_controller.h"
#include "user_controller.h"

class UserInterface
{
private:
    AdminController &adminController;
    UserController &userController;

    void GetCredentials();
    void HandleCredentials();
    bool isAdmin;

    void HandleAdmin();
    void PrintAdminMenu();
    void PrintEvents();
    void AddEvent();
    void DeleteEvent();
    void UpdateEvent();

    void HandleUser();
    void PrintUserMenu();
    void SeeEventsByMonth();
    void PrintEventList();
    void DeleteEventFromList();

    std::string InputTitle();
    std::string InputDescription();
    std::string InputLink();
    std::string InputDate();
    std::string InputTime();
    std::string InputPeople();

    std::string InputOldTitle();
    std::string InputOldDate();

    std::string InputMonth();

public:
    UserInterface(AdminController &adminController, UserController &userController):adminController(adminController), userController(userController){};

    void Run();
};

#endif //OOP_A4_5_916_SABAILA_CALIN_USER_INTERFACE_H
