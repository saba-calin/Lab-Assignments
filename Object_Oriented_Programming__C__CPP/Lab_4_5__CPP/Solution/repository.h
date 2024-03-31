#ifndef OOP_A4_5_916_SABAILA_CALIN_REPOSITORY_H
#define OOP_A4_5_916_SABAILA_CALIN_REPOSITORY_H

#include "domain.h"
#include "vector.h"

class Repository
{
private:
    vector <Event> events;

public:
    void AddEvent(Event e);
    void RemoveAtPosition(int idx);
    void UpdateAtPosition(int idx, Event e);
    void UpdateAttendance(std::string title, std::string date, int people);

    vector <Event>GetEvents();
};

#endif //OOP_A4_5_916_SABAILA_CALIN_REPOSITORY_H
//