#include "tests.h"

#include <iostream>

// This function tests the vector class
void Tests::TestVector()
{
    vector <int> v;
    v.push_back(1);
    assert(v[0] == 1);
    v.push_back(2);
    assert(v[1] == 2);
    v.pop_back();
    assert(v.size() == 1);
    assert(v.capacity() == 2);
    v.pop_back();

    try
    {
        v.pop_back();
    }
    catch (std::string &exception)
    {
        assert(exception == "Cannot pop any more elements");
    }
    try
    {
        v[0] = 1;
    }
    catch (std::string  &exception)
    {
        assert(exception == "Index 0 is out of range");
    }

    vector <Event> e;
    e.push_back(Event("1", "2", "3", "4", "5", 6));
}

// This function tests the domain class
void Tests::TestDomain()
{
    Event e = Event("1", "2", "3", "4", "5", 6);
    assert(e.GetTitle() == "1");
    assert(e.GetDescription() == "2");
    assert(e.GetLink() == "3");
    assert(e.GetDate() == "4");
    assert(e.GetTime() == "5");
    assert(e.GetPeople() == 6);

    e.SetTitle("7");
    e.SetDescription("8");
    e.SetLink("9");
    e.SetDate("10");
    e.SetTime("11");
    e.SetPeople(12);
    assert(e.GetTitle() == "7");
    assert(e.GetDescription() == "8");
    assert(e.GetLink() == "9");
    assert(e.GetDate() == "10");
    assert(e.GetTime() == "11");
    assert(e.GetPeople() == 12);
}

// This function tests the repository class
void Tests::TestRepository()
{
    Repository repo = Repository();

    try
    {
        vector <Event> v = repo.GetEvents();
    }
    catch (std::string &exception)
    {
        assert(exception == "The repository is empty");
    }
    repo.AddEvent(Event("1", "2", "3", "4", "5", 6));
    vector <Event> v = repo.GetEvents();
    assert(v[0].GetTitle() == "1");

    try
    {
        repo.UpdateAtPosition(1, Event("7", "8", "9", "10", "11", 12));
    }
    catch (std::string &exception)
    {
        assert(exception == "Index 1 is out of range");
    }
    repo.UpdateAtPosition(0, Event("7", "8", "9", "10", "11", 12));
    vector <Event> v1 = repo.GetEvents();
    assert(v1[0].GetTitle() == "7");

    repo.AddEvent(Event("1", "2", "3", "4", "5", 6));
    try
    {
        repo.RemoveAtPosition(2);
    }
    catch (std::string &exception)
    {
        assert(exception == "Index 2 is out of range");
    }
    repo.RemoveAtPosition(0);

    vector <Event> v2 = repo.GetEvents();
    assert(v2.size() == 1);
    repo.UpdateAttendance("1", "4", 1);
    assert(repo.GetEvents()[0].GetPeople() == 7);
}

// This function tests the TestGetEvents function from the controller class
void Tests::TestGetEvents()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    adminController.Add10Events();
    vector <Event> v = adminController.GetEvents();
    assert(v.size() == 10);
}

// This function tests the IsValidInt function from the controller class
void Tests::TestIsValidInt()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    assert(adminController.IsValidInt("fdas") == false);
    assert(adminController.IsValidInt("1") == true);
}

// This function tests the IsValidDate function from the controller class
void Tests::TestIsValidDate()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    assert(adminController.IsValidDate("") == false);
    assert(adminController.IsValidDate("0123456789") == false);
    assert(adminController.IsValidDate("0a/08/2024") == false);
    assert(adminController.IsValidDate("08/08/2024") == true);
}

// This function tests the IsValidTime function from the controller class
void Tests::TestIsValidTime()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    assert(adminController.IsValidTime("") == false);
    assert(adminController.IsValidTime("01234") == false);
    assert(adminController.IsValidTime("aa:aa") == false);
    assert(adminController.IsValidTime("12:00") == true);
}

// This function tests the AddEvent function from the controller class
void Tests::TestAddEvent()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    adminController.Add10Events();
    try
    {
        adminController.AddEvent("1", "2", "3", "4", "5", "6");
    }
    catch (std::string &exception)
    {
        assert(exception == "The date is not valid\n");
    }
    try
    {
        adminController.AddEvent("1", "2", "3", "08/08/2024", "5", "6");
    }
    catch (std::string &exception)
    {
        assert(exception == "The time is not valid\n");
    }
    try
    {
        adminController.AddEvent("1", "2", "3", "08/08/2024", "18:00", "-6");
    }
    catch (std::string &exception)
    {
        assert(exception == "The number of people is not valid\n");
    }

    adminController.AddEvent("1", "2", "3", "08/08/2024", "18:00", "6");
    try
    {
        adminController.AddEvent("1", "2", "3", "08/08/2024", "18:00", "6");
    }
    catch (std::string &exception)
    {
        assert(exception == "The event has already been added\n");
    }
}

// This function tests the DeleteEvent function from the controller class
void Tests::TestDeleteEvent()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    adminController.Add10Events();
    try
    {
        adminController.DeleteEvent("1", "2");
    }
    catch (std::string &exception)
    {
        assert(exception == "The date is not valid\n");
    }
    try
    {
        adminController.DeleteEvent("1", "08/08/2024");
    }
    catch (std::string &exception)
    {
        assert(exception == "No event with the given identifiers was found\n");
    }

    adminController.AddEvent("1", "2", "3", "08/08/2024", "18:00", "6");
    adminController.DeleteEvent("1", "08/08/2024");
    vector <Event> v = adminController.GetEvents();
    assert(v.size() == 10);
}

// This function tests the UpdateEvent function from the controller class
void Tests::TestUpdateEvent()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    adminController.Add10Events();
    try
    {
        adminController.UpdateEvent("1", "2", "3", "4", "5", "6", "7", "8");
    }
    catch (std::string &exception)
    {
        assert(exception == "The old date is not valid\n");
    }
    try
    {
        adminController.UpdateEvent("1", "08/08/2024", "3", "4", "5", "6", "7", "8");
    }
    catch (std::string &exception)
    {
        assert(exception == "The date is not valid\n");
    }
    try
    {
        adminController.UpdateEvent("1", "08/08/2024", "3", "4", "5", "08/08/2024", "7", "8");
    }
    catch (std::string &exception)
    {
        assert(exception == "The time is not valid\n");
    }
    try
    {
        adminController.UpdateEvent("1", "08/08/2024", "3", "4", "5", "08/08/2024", "18:00", "-8");
    }
    catch (std::string &exception)
    {
        assert(exception == "The number of people is not valid\n");
    }
    try
    {
        adminController.UpdateEvent("1", "08/08/2024", "3", "4", "5", "08/08/2024", "18:00", "8");
    }
    catch (std::string &exception)
    {
        assert(exception == "No event with the given identifiers was found\n");
    }

    adminController.UpdateEvent("Lollapalooza", "01/08/2024", "3", "4", "5", "08/08/2024", "18:00", "8");
    vector <Event> v = adminController.GetEvents();
    assert(v[0].GetPeople() == 8);
}

// This function tests the UpdateAttendance function from the controller class
void Tests::TestUpdateAttendance()
{
    Repository repo;
    AdminController adminController = AdminController(repo);
    adminController.Add10Events();
    adminController.UpdateAttendance("Lollapalooza", "01/08/2024", 1);
    assert(adminController.GetEvents()[0].GetPeople() == 225001);
}

// This function tests the GetDay function from the controller class
void Tests::TestGetDay()
{
    Repository repo;
    UserController userController(repo);
    assert(userController.GetDay("28/03/2024") == 28);
}

// This function tests the GetMonth function from the controller class
void Tests::TestGetMonth()
{
    Repository repo;
    UserController userController(repo);
    assert(userController.GetMonth("28/03/2024") == 3);
}

// This function tests the GetYear function from the controller class
void Tests::TestGetYear()
{
    Repository repo;
    UserController userController(repo);
    assert(userController.GetYear("28/03/2024") == 2024);
}

// This function tests the IsValidMonth function from the controller class
void Tests::TestIsValidMonth()
{
    Repository repo;
    UserController userController(repo);
    assert(userController.IsValidMonth("") == false);
    assert(userController.IsValidMonth("..") == false);
    assert(userController.IsValidMonth("03") == true);
}

// This function tests the Swap function from the controller class
void Tests::TestSwap()
{
    Repository repo;
    AdminController adminController(repo);
    UserController userController(repo);
    adminController.Add10Events();
    vector <Event> v = adminController.GetEvents();
    userController.Swap(v[0], v[1]);
    assert(v[0].GetPeople() == 75000);
}

// This function tests the AddUserEvent function from the controller class
void Tests::TestAddUserEvent()
{
    Repository repo;
    UserController userController(repo);
    userController.AddEvent(Event("1", "2", "3", "4", "5", 6));
    assert(userController.GetEventList().size() == 1);
}

// This function tests the GetEventList function from the controller class
void Tests::TestGetEventList()
{
    Repository repo;
    UserController userController(repo);
    try
    {
        userController.GetEventList();
    }
    catch (std::string &exception)
    {
        assert(exception == "The list of events is empty\n");
    }
    userController.AddEvent(Event("1", "2", "3", "4", "5", 6));
    assert(userController.GetEventList().size() == 1);
}

// This function tests the TestUpdateUserAttendance function from the controller class
void Tests::TestUpdateUserAttendance()
{
    Repository repo;
    UserController userController(repo);
    userController.AddEvent(Event("1", "2", "3", "4", "5", 6));
    userController.UpdateAttendance("1", "4", 1);
    assert(userController.GetEventList()[0].GetPeople() == 7);
}

// This function tests the TestDeleteUserEvent function from the controller class
void Tests::TestDeleteUserEvent()
{
    Repository repo;
    UserController userController(repo);
    try
    {
        userController.DeleteEvent("1", "2");
    }
    catch (std::string &exception)
    {
        assert(exception == "The list of events is empty\n");
    }
    userController.AddEvent(Event("1", "2", "3", "4", "5", 6));
    userController.AddEvent(Event("7", "8", "9", "10", "11", 12));
    userController.DeleteEvent("1", "4");
    assert(userController.GetEventList().size() == 1);
    try
    {
        userController.DeleteEvent("1", "2");
    }
    catch (std::string &exception)
    {
        assert(exception == "No event with the given identifiers was found\n");
    }
}

// This function tests the GetEventsByMonth function from the controller class
void Tests::TestGetEventsByMonth()
{
    Repository repo;
    UserController userController(repo);
    AdminController adminController(repo);
    adminController.Add10Events();
    adminController.AddEvent("Outside Lands", "San Francisco", "https://sfoutsidelands.com/", "09/08/2025", "21:00", "50000");
    adminController.AddEvent("Title", "San Francisco", "https://sfoutsidelands.com/", "09/08/2024", "21:00", "50000");
    try
    {
        userController.GetEventsByMonth("1");
    }
    catch (std::string &exception)
    {
        assert(exception == "The month is not valid\n");
    }
    vector <Event> v = userController.GetEventsByMonth("");
    assert(v.size() == 12);
}

// This function tests the controller class
void Tests::TestAdminController()
{
    TestGetEvents();
    TestIsValidInt();
    TestIsValidDate();
    TestIsValidTime();
    TestAddEvent();
    TestDeleteEvent();
    TestUpdateEvent();
    TestUpdateAttendance();
}

// This function tests the controller class
void Tests::TestUserController()
{
    TestGetDay();
    TestGetMonth();
    TestGetYear();
    TestIsValidMonth();
    TestSwap();
    TestAddUserEvent();
    TestGetEventList();
    TestUpdateUserAttendance();
    TestDeleteUserEvent();
    TestGetEventsByMonth();
}

// This function runs all the tests
void Tests::RunAllTests()
{
    TestVector();
    TestDomain();
    TestRepository();
    TestAdminController();
    TestUserController();
}
