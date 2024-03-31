#include "repository.h"

// This function adds an event to the repository
// @param e: an event that will be added to the repository
// @return: none
void Repository::AddEvent(Event e)
{
    this -> events.push_back(e);
}

// This function returns all the events from the repository
// @param: none
// @throws: a string exception if the repository is empty
// @return: a vector of events
vector <Event>Repository::GetEvents()
{
    if (this -> events.size() == 0)
        throw std::string("The repository is empty");

    vector <Event> v;
    for (int i = 0; i < this -> events.size(); i++)
    {
        v.push_back(this -> events[i]);
    }
    return v;
}

// This function deletes an event from the repository
// @param idx: an integer representing the position of the event that will be deleted
// @throws: a string exception if the index is out of range
// @return: none
void Repository::RemoveAtPosition(int idx)
{
    if (idx < 0 || idx >= this -> events.size())
        throw std::string("Index " + std::to_string(idx) + " is out of range");

    for (int i = idx; i < this -> events.size() - 1; i++)
    {
        this -> events[i] = this -> events[i + 1];
    }
    this -> events.pop_back();
}

// This function updates an event from the repository
// @param idx: an integer representing the position of the event that will be updated
// @param e: an event that will replace the old event
// @throws: a string exception if the index is out of range
// @return: none
void Repository::UpdateAtPosition(int idx, Event e)
{
    if (idx < 0 || idx >= this -> events.size())
        throw std::string("Index " + std::to_string(idx) + " is out of range");

    this -> events[idx].SetTitle(e.GetTitle());
    this -> events[idx].SetDescription(e.GetDescription());
    this -> events[idx].SetLink(e.GetLink());
    this -> events[idx].SetDate(e.GetDate());
    this -> events[idx].SetTime(e.GetTime());
    this -> events[idx].SetPeople(e.GetPeople());
}

// This function updates the number of people that will attend an event
// @param title: a string representing the title of the event
// @param date: a string representing the date of the event
// @param people: an integer representing the number of people that will attend the event
// @return: none
void Repository::UpdateAttendance(std::string title, std::string date, int people)
{
    for (int i = 0; i < this -> events.size(); i++)
    {
        if (this -> events[i].GetTitle() == title && this -> events[i].GetDate() == date)
        {
            this -> events[i].SetPeople(this -> events[i].GetPeople() + people);
        }
    }
}
