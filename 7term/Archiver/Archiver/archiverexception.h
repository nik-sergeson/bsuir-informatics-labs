#ifndef ARCHIVEREXCEPTION
#define ARCHIVEREXCEPTION
#include <stdexcept>
#include <string>
using namespace std;

class ArchiverException : public runtime_error
{
public:
    ArchiverException(const string& msg): runtime_error(msg) {}
};


#endif // ARCHIVEREXCEPTION

