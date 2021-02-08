#ifndef TASK_INCLUDED
#define TASK_INCLUDED
#include "user.h"

class Meeting{
public:
    Meeting(User &usr,std::string description);
    void ChangeTime(time_t newdate);
private:
    time_t date;
    std::string description;
    User user;
};

#endif // TASK_INCLUDED
