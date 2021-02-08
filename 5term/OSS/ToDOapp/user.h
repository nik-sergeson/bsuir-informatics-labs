#ifndef USER_H_INCLUDED
#define USER_H_INCLUDED
#include <string>

class User{
public:
    User();
    User(std::string name,std::string secondname,std::string phone);
private:
    std::string name;
    std::string secondname;
    std::string phone;
};

#endif // USER_H_INCLUDED
