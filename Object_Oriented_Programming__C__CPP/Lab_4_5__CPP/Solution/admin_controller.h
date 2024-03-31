#ifndef OOP_A4_5_916_SABAILA_CALIN_ADMIN_CONTROLLER_H
#define OOP_A4_5_916_SABAILA_CALIN_ADMIN_CONTROLLER_H

#include "repository.h"
#include "vector.h"

class AdminController
{
private:
    Repository &repo;

public:
    AdminController(Repository &repo):repo(repo){};

    void Add10Events();
    void AddEvent(std::string title, std::string description, std::string link, std::string date, std::string time, std::string people);
    void DeleteEvent(std::string title, std::string date);
    void UpdateEvent(std::string oldTitle, std::string oldDate, std::string title, std::string description, std::string link, std::string date, std::string time, std::string people);
    void UpdateAttendance(std::string title, std::string date, int people);

    bool IsValidDate(std::string date);
    bool IsValidTime(std::string time);
    bool IsValidInt(std::string people);

    vector <Event> GetEvents();
};

#endif //OOP_A4_5_916_SABAILA_CALIN_ADMIN_CONTROLLER_H
