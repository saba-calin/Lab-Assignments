#ifndef OOP_A4_5_916_SABAILA_CALIN_TESTS_H
#define OOP_A4_5_916_SABAILA_CALIN_TESTS_H

#include <string>
#include <cassert>


#include "vector.h"
#include "domain.h"
#include "repository.h"
#include "admin_controller.h"
#include "user_controller.h"

class Tests
{
private:
    void TestVector();
    void TestDomain();
    void TestRepository();
    void TestAdminController();
    void TestUserController();

    void TestGetEvents();
    void TestIsValidInt();
    void TestIsValidDate();
    void TestIsValidTime();
    void TestAddEvent();
    void TestDeleteEvent();
    void TestUpdateEvent();
    void TestUpdateAttendance();

    void TestGetDay();
    void TestGetMonth();
    void TestGetYear();
    void TestIsValidMonth();
    void TestSwap();
    void TestAddUserEvent();
    void TestGetEventList();
    void TestUpdateUserAttendance();
    void TestDeleteUserEvent();
    void TestGetEventsByMonth();

public:
    void RunAllTests();
};

#endif //OOP_A4_5_916_SABAILA_CALIN_TESTS_H
