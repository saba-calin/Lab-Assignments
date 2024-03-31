#ifndef OOP_A4_5_916_SABAILA_CALIN_USER_CONTROLLER_H
#define OOP_A4_5_916_SABAILA_CALIN_USER_CONTROLLER_H

#include "repository.h"
#include "vector.h"
#include "domain.h"

class UserController
{
private:
    Repository &repo;
    vector <Event> eventList;

public:
    UserController(Repository &repo):repo(repo){};

    vector <Event> GetEventsByMonth(std::string month);
    vector <Event> GetEventList();

    void AddEvent(Event e);
    void UpdateAttendance(std::string title, std::string date, int people);
    void DeleteEvent(std::string title, std::string date);

    bool IsValidMonth(std::string month);
    int GetDay(std::string date);
    int GetMonth(std::string date);
    int GetYear(std::string date);
    void Swap(Event &x, Event &y);
};

#endif //OOP_A4_5_916_SABAILA_CALIN_USER_CONTROLLER_H
