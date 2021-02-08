#include "meeting.h"
#include "user.h"
#include <string>

Meeting::Meeting(User &usr,std::string description){
    this->user=user;
    this->description=description;
}

void Meeting::ChangeTime(time_t newdate){
    date=newdate;
}
