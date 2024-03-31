#ifndef OOP_A4_5_916_SABAILA_CALIN_DOMAIN_H
#define OOP_A4_5_916_SABAILA_CALIN_DOMAIN_H

#include <string>

class Event
{
private:
    std::string title, description, link, date, time;
    int people;

public:
    Event(std::string title, std::string description, std::string link, std::string date, std::string time, int people);

    void SetTitle(std::string title);
    void SetDescription(std::string description);
    void SetLink(std::string link);
    void SetDate(std::string date);
    void SetTime(std::string time);
    void SetPeople(int people);

    std::string GetTitle();
    std::string GetDescription();
    std::string GetLink();
    std::string GetDate();
    std::string GetTime();
    int GetPeople();
};

#endif //OOP_A4_5_916_SABAILA_CALIN_DOMAIN_H
