#include "user_controller.h"
#include "domain.h"

// This function returns the events that are scheduled for a given month ordered by date,
// or all the events if the month is not specified
// @param month: a string representing the month for which the events are scheduled
// @return: a vector with the events that are scheduled for the given month
vector<Event> UserController::GetEventsByMonth(std::string month)
{
    if (month != "" && IsValidMonth(month) == false)
        throw std::string("The month is not valid\n");

    // Getting the vector
    vector <Event> v = this -> repo.GetEvents();
    vector <Event> vect;
    for (int i = 0; i < v.size(); i++)
    {
        if ((v[i].GetDate()[3] == month[0] && v[i].GetDate()[4] == month[1]) || month == "")
        {
            vect.push_back(v[i]);
        }
    }

    // Sorting the vector
    for (int i = 0; i < vect.size() - 1; i++)
    {
        for (int j = i + 1; j < vect.size(); j++)
        {
            if (GetYear(vect[i].GetDate()) > GetYear(vect[j].GetDate()))
            {
                Swap(vect[i], vect[j]);
            }
            else if ((GetYear(vect[i].GetDate()) == GetYear(vect[j].GetDate())) && (GetMonth(vect[i].GetDate()) > GetMonth(vect[j].GetDate())))
            {
                Swap(vect[i], vect[j]);
            }
            else if ((GetYear(vect[i].GetDate()) == GetYear(vect[j].GetDate())) && (GetMonth(vect[i].GetDate()) == GetMonth(vect[j].GetDate())) && (GetDay(vect[i].GetDate())) > GetDay(vect[j].GetDate()))
            {
                Swap(vect[i], vect[j]);
            }
        }
    }

    return vect;
}

// This function returns the list of events
// @param: none
// @throws: a string exception if the list of events is empty
// @return: a vector with all the events
vector <Event> UserController::GetEventList()
{
    if (this -> eventList.size() == 0)
        throw std::string("The list of events is empty\n");

    vector <Event> v;
    for (int i = 0; i < this -> eventList.size(); i++)
    {
        v.push_back(this -> eventList[i]);
    }
    return v;
}

// This function updates the number of people that will attend an event
// @param title: a string representing the title of the event
// @param date: a string representing the date of the event
// @param people: an integer representing the number of people that will attend the event
// @return: none
void UserController::UpdateAttendance(std::string title, std::string date, int people)
{
    for (int i = 0; i < this -> eventList.size(); i++)
    {
        if (this -> eventList[i].GetTitle() == title && this -> eventList[i].GetDate() == date)
        {
            this -> eventList[i].SetPeople(this -> eventList[i].GetPeople() + people);
        }
    }
}

// This function adds an event to the list of events
// @param e: an event that will be added to the list of events
// @return: none
void UserController::AddEvent(Event e)
{
    this -> eventList.push_back(e);
}

// This function validates a month
// @param month: a string representing the month
// @return: true if the month is valid, false otherwise
bool UserController::IsValidMonth(std::string month)
{
    if (month.size() != 2)
        return false;
    for (int i = 0; i < month.size(); i++)
    {
        if (month[i] < '0' or month[i] > '9')
        {
            return false;
        }
    }

    return true;
}

// This function returns the day from a date
// @param date: a string representing the date
// @return: an integer representing the day
int UserController::GetDay(std::string date)
{
    int day = 10 * (date[0] - '0') + (date[1] - '0');
    return day;
}

// This function returns the month from a date
// @param date: a string representing the date
// @return: an integer representing the month
int UserController::GetMonth(std::string date)
{
    int month = 10 * (date[3] - '0') + (date[4] - '0');
    return month;
}

// This function returns the year from a date
// @param date: a string representing the date
// @return: an integer representing the year
int UserController::GetYear(std::string date)
{
    int year = 1000 * (date[6] - '0') + 100 * (date[7] - '0') + 10 * (date[8] - '0') + (date[9] - '0');
    return year;
}

// This function swaps two events
// @param x: a reference to the first event
// @param y: a reference to the second event
// @return: none
void UserController::Swap(Event &x, Event &y)
{
    Event temp = x;
    x = y;
    y = temp;
}

// This function deletes an event from the list of events
// @param title: a string representing the title of the event
// @param date: a string representing the date of the event
// @return: none
void UserController::DeleteEvent(std::string title, std::string date)
{
    if (this -> eventList.size() == 0)
        throw std::string("The list of events is empty\n");

    for (int i = 0; i < this -> eventList.size(); i++)
    {
        if (this -> eventList[i].GetTitle() == title && this -> eventList[i].GetDate() == date)
        {
            for (int j = i; j < this -> eventList.size() - 1; j++)
            {
                this -> eventList[j] = this -> eventList[j + 1];

            }
            this -> eventList.pop_back();

            return;
        }
    }

    throw std::string("No event with the given identifiers was found\n");
}
