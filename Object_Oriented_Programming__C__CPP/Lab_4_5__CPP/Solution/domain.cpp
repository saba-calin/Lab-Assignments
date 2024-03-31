#include "domain.h"

// This is the default constructor of the Event class
// It initializes the title, description, link, date, time and people of the event
// @param title: a string representing the title of the event
// @param description: a string representing the description of the event
// @param link: a string representing the link of the event
// @param date: a string representing the date of the event
// @param time: a string representing the time of the event
// @param people: an integer representing the number of people that will attend the event
// @return: none
Event::Event(std::string title, std::string description, std::string link, std::string date, std::string time, int people)
{
    this -> title = title;
    this -> description = description;
    this -> link = link;
    this -> date = date;
    this -> time = time;
    this -> people = people;
}

// This function sets the title of the event
// @param title: a string representing the title of the event
// @return: none
void Event::SetTitle(std::string title)
{
    this -> title = title;
}

// This function sets the description of the event
// @param description: a string representing the description of the event
// @return: none
void Event::SetDescription(std::string description)
{
    this -> description = description;
}

// This function sets the link of the event
// @param link: a string representing the link of the event
// @return: none
void Event::SetLink(std::string link)
{
    this -> link = link;
}

// This function sets the date of the event
// @param date: a string representing the date of the event
// @return: none
void Event::SetDate(std::string date)
{
    this -> date = date;
}

// This function sets the time of the event
// @param time: a string representing the time of the event
// @return: none
void Event::SetTime(std::string time)
{
    this -> time = time;
}

// This function sets the number of people that will attend the event
// @param people: an integer representing the number of people that will attend the event
// @return: none
void Event::SetPeople(int people)
{
    this -> people = people;
}

// This function returns the title of the event
// @param: none
// @return: a string representing the title of the event
std::string Event::GetTitle()
{
    return this -> title;
}

// This function returns the description of the event
// @param: none
// @return: a string representing the description of the event
std::string Event::GetDescription()
{
    return this -> description;
}

// This function returns the link of the event
// @param: none
// @return: a string representing the link of the event
std::string Event::GetLink()
{
    return this -> link;
}

// This function returns the date of the event
// @param: none
// @return: a string representing the date of the event
std::string Event::GetDate()
{
    return this -> date;
}

// This function returns the time of the event
// @param: none
// @return: a string representing the time of the event
std::string Event::GetTime()
{
    return this -> time;
}

// This function returns the number of people that will attend the event
// @param: none
// @return: an integer representing the number of people that will attend the event
int Event::GetPeople()
{
    return this -> people;
}