#include "admin_controller.h"

// This function validates an event and adds it to the repository
// @param title: a string representing the title of the event
// @param description: a string representing the description of the event
// @param link: a string representing the link of the event
// @param date: a string representing the date of the event
// @param time: a string representing the time of the event
// @param people: a string representing the number of people that will attend the event
// @throws: a string exception if the date, time or number of people are not valid
// @throws: a string exception if the event has already been added
// @return: none
void AdminController::AddEvent(std::string title, std::string description, std::string link, std::string date, std::string time, std::string people)
{
    if (IsValidDate(date) == false)
        throw std::string("The date is not valid\n");
    if (IsValidTime(time) == false)
        throw std::string("The time is not valid\n");
    if (IsValidInt(people) == false)
        throw std::string("The number of people is not valid\n");

    vector <Event> v = GetEvents();
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i].GetTitle() == title && v[i].GetDate() == date)
        {
            throw std::string("The event has already been added\n");
        }
    }

    Event e = Event(title, description, link, date, time, stoi(people));
    this -> repo.AddEvent(e);
}

// This function deletes an event from the repository
// @param title: a string representing the title of the event
// @param date: a string representing the date of the event
// @throws: a string exception if the date is not valid
// @throws: a string exception if the event with the given identifiers was not found
// @return: none
void AdminController::DeleteEvent(std::string title, std::string date)
{
    if (IsValidDate(date) == false)
        throw std::string("The date is not valid\n");

    vector <Event> v = GetEvents();
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i].GetTitle() == title && v[i].GetDate() == date)
        {
            this -> repo.RemoveAtPosition(i);
            return;
        }
    }
    throw std::string("No event with the given identifiers was found\n");
}

// This function updates an event from the repository
// @param oldTitle: a string representing the title of the event that will be updated
// @param oldDate: a string representing the date of the event that will be updated
// @param title: a string representing the new title of the event
// @param description: a string representing the new description of the event
// @param link: a string representing the new link of the event
// @param date: a string representing the new date of the event
// @param time: a string representing the new time of the event
// @param people: a string representing the new number of people that will attend the event
// @throws: a string exception if the old date, date, time or number of people are not valid
// @throws: a string exception if the event with the given identifiers was not found
// @return: none
void AdminController::UpdateEvent(std::string oldTitle, std::string oldDate, std::string title, std::string description, std::string link, std::string date, std::string time, std::string people)
{
    if (IsValidDate(oldDate) == false)
        throw std::string("The old date is not valid\n");
    if (IsValidDate(date) == false)
        throw std::string("The date is not valid\n");
    if (IsValidTime(time) == false)
        throw std::string("The time is not valid\n");
    if (IsValidInt(people) == false)
        throw std::string("The number of people is not valid\n");

    vector <Event> v = GetEvents();
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i].GetTitle() == oldTitle && v[i].GetDate() == oldDate)
        {
            this -> repo.UpdateAtPosition(i, Event(title, description, link, date, time, stoi(people)));
            return;
        }
    }
    throw std::string("No event with the given identifiers was found\n");
}

// This function returns all the events from the repository
// @param: none
// @return: a vector with all the events from the repository
vector <Event>AdminController::GetEvents()
{
    return this -> repo.GetEvents();
}

// This function checks if a string is a valid integer
// @param people: a string representing the number of people that will attend the event
// @return: true if the string is a valid integer, false otherwise
bool AdminController::IsValidInt(std::string people)
{
    for (int i = 0; i < people.size(); i++)
    {
        if (people[i] < '0' || people[i] > '9')
        {
            return false;
        }
    }
    return true;
}

// This function checks if a string is a valid date
// @param date: a string representing the date of the event
// @return: true if the string is a valid date, false otherwise
bool AdminController::IsValidDate(std::string date)
{
    if (date.size() != 10)
        return false;
    if (date[2] != '/' || date[5] != '/')
        return false;
    for (int i = 0; i < date.size(); i++)
    {
        if (i == 2 || i == 5)
            continue;
        if (date[i] < '0' || date[i] > '9')
            return false;
    }

    return true;
}

// This function checks if a string is a valid time
// @param time: a string representing the time of the event
// @return: true if the string is a valid time, false otherwise
bool AdminController::IsValidTime(std::string time)
{
    if (time.size() != 5)
        return false;
    if (time[2] != ':')
        return false;
    for (int i = 0; i < time.size(); i++)
    {
        if (i == 2)
            continue;
        if (time[i] < '0' || time[i] > '9')
            return false;
    }

    return true;
}

// This function adds 10 events to the repository
// @param: none
// @return: none
void AdminController::Add10Events()
{
    Event e1 = Event("Lollapalooza", "Chicago", "https://www.lollapalooza.com/", "01/08/2024", "15:30", 225000);       this -> repo.AddEvent(e1);
    Event e2 = Event("Rolling Load", "Vienna", "https://europe.rollingloud.com/", "05/07/2024", "12:00", 75000);       this -> repo.AddEvent(e2);
    Event e3 = Event("Beach Please", "Costinesti", "https://beach-please.ro/", "11/07/2024", "18:00", 30000);          this -> repo.AddEvent(e3);
    Event e4 = Event("Coachella", "Lake Eldorado", "https://www.coachella.com/", "12/04/2024", "20:00", 120000);       this -> repo.AddEvent(e4);
    Event e5 = Event("Saga", "Bucharest", "https://www.sagafestival.com/", "05/06/2024", "15:50", 35000);              this -> repo.AddEvent(e5);
    Event e6 = Event("Untold", "Cluj-Napoca", "https://untold.com/", "08/08/2024", "17:00", 50000);                    this -> repo.AddEvent(e6);
    Event e7 = Event("Electric Castle", "Cluj-Napoca", "https://electriccastle.ro/", "17/07/2024", "19:45", 25000);    this -> repo.AddEvent(e7);
    Event e8 = Event("Summerfest", "Milwaukee", "https://www.summerfest.com/", "20/06/2024", "17:00", 150000);         this -> repo.AddEvent(e8);
    Event e9 = Event("Wonderbus", "Columbus", "https://www.wonderbusfest.com/", "25/08/2024", "18:30", 75000);         this -> repo.AddEvent(e9);
    Event e10 = Event("Outside Lands", "San Francisco", "https://sfoutsidelands.com/", "09/08/2024", "21:00", 50000);  this -> repo.AddEvent(e10);
}

// This function updates the number of people that will attend an event
// @param title: a string representing the title of the event
// @param date: a string representing the date of the event
// @param people: an integer representing the new number of people that will attend the event
// @return: none
void AdminController::UpdateAttendance(std::string title, std::string date, int people)
{
    this -> repo.UpdateAttendance(title, date, people);
}
