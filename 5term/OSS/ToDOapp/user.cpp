    #include "user.h"
    #include <string>
    #include <iostream>

    User::User(std::string name,std::string secondname,std::string phone){
        this->name=name;
        this->secondname=secondname;
        this->phone=phone;
        std::cout<<"Changed";
    }

    User::User(){}
