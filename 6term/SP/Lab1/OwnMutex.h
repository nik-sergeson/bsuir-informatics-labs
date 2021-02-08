#ifndef OWNMUTEX_H_INCLUDED
#define OWNMUTEX_H_INCLUDED
#include <windows.h>
#include <deque>

class ownmutex{
private:
    volatile bool busy;
    long synchronize;
    deque<DWORD> idqueue;
    DWORD current;

public:

    ownmutex(){
        busy=false;
        synchronize=0;
        current=0;
    }

    void Lock(){
        while(synchronize);
        InterlockedIncrement(&synchronize);
        idqueue.push_back(GetCurrentThreadId());
        if(current!=GetCurrentThreadId()){
            while(busy||idqueue.front()!=GetCurrentThreadId())
                Sleep(10);
            busy=true;
            current=idqueue.front();
            idqueue.pop_front();
        }
        else{
            idqueue.pop_back();
        }
        InterlockedDecrement(&synchronize);
    }

    void Unlock(){
        if(current==GetCurrentThreadId()){
            busy=false;
        }
    }

};

#endif // OWNMUTEX_H_INCLUDED
