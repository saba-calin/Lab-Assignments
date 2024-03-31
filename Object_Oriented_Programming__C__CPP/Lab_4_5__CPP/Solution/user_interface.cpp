#include <iostream>

#include "user_interface.h"

void UserInterface::GetCredentials()
{
    std::cout << "\n";
    std::cout << "Type \'exit\' to close the application\n";
    std::cout << "Would you like to log in as an administrator? (y/n)\n";
    std::string option;
    std::getline(std::cin, option);

    while (option != "n" && option != "y" && option != "exit")
    {
        std::cout << "Invalid option, please try again\n";
        std::getline(std::cin, option);
    }

    if (option == "y")
        this -> isAdmin = true;
    else if (option == "n")
        this -> isAdmin = false;
    else
    {
        std::cout << "Closing the application...\n";
        exit(0);
    }

    HandleCredentials();
}

void UserInterface::HandleCredentials()
{
    if (this -> isAdmin == true)
    {
        HandleAdmin();
    }
    else
    {
        HandleUser();
    }
}

void UserInterface::Run()
{
    this -> adminController.Add10Events();
    GetCredentials();
}

void UserInterface::PrintUserMenu()
{
    std::cout << "\n";
    std::cout << "Press 1 to see all events in a given month\n";
    std::cout << "Press 2 to see the list of events\n";
    std::cout << "Press 3 to delete an event from the list of events\n";
    std::cout << "Type \'exit\' to log out\n";
}

void UserInterface::HandleUser()
{
    while (true) {
        PrintUserMenu();

        std::string option;
        std::getline(std::cin, option);

        try
        {
            if (option == "1")       SeeEventsByMonth();
            else if (option == "2")  PrintEventList();
            else if (option == "3")  DeleteEventFromList();
            else if (option == "exit")
            {
                std::cout << "Logging out...\n";
                GetCredentials();
            }
            else
            {
                std::cout << "Invalid input, please try again\n";
            }
        }
        catch (std::string &exception)
        {
            std::cout << exception << "\n";
        }
    }
}

void UserInterface::SeeEventsByMonth()
{
    std::string month;
    month = InputMonth();

    std::cout << "Type \'exit\' to exit at any time\n";
    vector <Event> v = this -> userController.GetEventsByMonth(month);
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << "\n";
        std::cout << "title: " << v[i].GetTitle() << ", description: " << v[i].GetDescription() << ", date: "
        << v[i].GetDate() << ", time: " << v[i].GetTime() << ", people: " << v[i].GetPeople() << "\n";
        std::cout << "link: " << v[i].GetLink() << "\n";

        std::cout << "Would you like to add this event to the list? (y/n)\n";
        std::string option;
        std::getline(std::cin, option);
        while (option != "n" && option != "y" && option != "exit")
        {
            std::cout << "Invalid option, please try again\n";
            std::getline(std::cin, option);
        }

        if (option == "y")
        {
            this -> userController.AddEvent(v[i]);
            this -> userController.UpdateAttendance(v[i].GetTitle(), v[i].GetDate(), 1);
            this -> adminController.UpdateAttendance(v[i].GetTitle(), v[i].GetDate(), 1);
            v[i].SetPeople(v[i].GetPeople() + 1);
        }
        else if (option == "exit")
        {
            break;
        }

        if (i == v.size() - 1)
        {
            i = -1;
        }
    }
}

void UserInterface::PrintEventList()
{
    vector <Event> v = this -> userController.GetEventList();
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << "title: " << v[i].GetTitle() << ", description: " << v[i].GetDescription() << ", link: " <<
        v[i].GetLink() << ", date: " << v[i].GetDate() << ", time: " << v[i].GetTime() << ", people: " << v[i].GetPeople() << "\n";
    }
}

void UserInterface::DeleteEventFromList()
{
    std::string title = InputTitle();
    std::string date = InputDate();

    this -> userController.DeleteEvent(title, date);
    this -> userController.UpdateAttendance(title, date, -1);
    this -> adminController.UpdateAttendance(title, date, -1);
}

void UserInterface::PrintAdminMenu()
{
    std::cout << "\n";
    std::cout << "Press 1 to display all events\n";
    std::cout << "Press 2 to add an event\n";
    std::cout << "Press 3 to delete an event\n";
    std::cout << "Press 4 to update an event\n";
    std::cout << "Type \'exit\' to log out\n";
}

void UserInterface::HandleAdmin()
{
    while (true)
    {
        PrintAdminMenu();

        std::string option;
        std::getline(std::cin, option);

        try
        {
            if (option == "1")       PrintEvents();
            else if (option == "2")  AddEvent();
            else if (option == "3")  DeleteEvent();
            else if (option == "4")  UpdateEvent();
            else if (option == "exit")
            {
                std::cout << "Logging out...\n";
                GetCredentials();
            }
            else
            {
                std::cout << "Invalid input, please try again\n";
            }
        }
        catch (std::string &exception)
        {
            std::cout << exception << "\n";
        }
    }
}

void UserInterface::PrintEvents()
{
    vector <Event> v = this -> adminController.GetEvents();
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << "title: " << v[i].GetTitle() << ", description: " << v[i].GetDescription() << ", link: " <<
        v[i].GetLink() << ", date: " << v[i].GetDate() << ", time: " << v[i].GetTime() << ", people: " << v[i].GetPeople() << "\n";
    }
}

void UserInterface::AddEvent()
{
    std::string title = InputTitle();
    std::string description = InputDescription();
    std::string link = InputLink();
    std::string date = InputDate();
    std::string time = InputTime();
    std::string people = InputPeople();

    this -> adminController.AddEvent(title, description, link, date, time, people);
}

void UserInterface::DeleteEvent()
{
    std::string title = InputTitle();
    std::string date = InputDate();

    this -> adminController.DeleteEvent(title, date);
}

void UserInterface::UpdateEvent()
{
    std::string oldTitle = InputOldTitle();
    std::string oldDate = InputOldDate();
    std::string title = InputTitle();
    std::string description = InputDescription();
    std::string link = InputLink();
    std::string date = InputDate();
    std::string time = InputTime();
    std::string people = InputPeople();

    this -> adminController.UpdateEvent(oldTitle, oldDate, title, description, link, date, time, people);
}

std::string UserInterface::InputTitle()
{
    std::string title;
    std::cout << "Enter the title of the event\n";
    std::getline(std::cin, title);
    return title;
}

std::string UserInterface::InputDescription()
{
    std::string description;
    std::cout << "Enter the description of the event\n";
    std::getline(std::cin, description);
    return description;
}

std::string UserInterface::InputLink()
{
    std::string link;
    std::cout << "Enter the link of the event\n";
    std::getline(std::cin, link);
    return link;
}

std::string UserInterface::InputDate()
{
    std::string date;
    std::cout << "Enter the date of the event (dd/mm/yyyy format)\n";
    std::getline(std::cin, date);
    return date;
}

std::string UserInterface::InputTime()
{
    std::string time;
    std::cout << "Enter the time of the event (hh:mm format)\n";
    std::getline(std::cin, time);
    return time;
}

std::string UserInterface::InputPeople()
{
    std::string people;
    std::cout << "Enter the number of people attending the event\n";
    std::getline(std::cin, people);
    return people;
}

std::string UserInterface::InputOldTitle()
{
    std::string oldTitle;
    std::cout << "Enter the old title of the event\n";
    std::getline(std::cin, oldTitle);
    return oldTitle;
}

std::string UserInterface::InputOldDate()
{
    std::string oldDate;
    std::cout << "Enter the old date of the event (dd/mm/yyyy format)\n";
    std::getline(std::cin, oldDate);
    return oldDate;
}

std::string UserInterface::InputMonth()
{
    std::string month;
    std::cout << "Enter the month (mm format)\n";
    std::getline(std::cin, month);
    return month;
}
