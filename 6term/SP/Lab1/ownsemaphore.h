#ifndef OWNSEMAPHORE_H_INCLUDED
#define OWNSEMAPHORE_H_INCLUDED
#include <deque>
#include <set>
using namespace std;

class ownsemaphore{
private:
    int capacity;
    volatile long synchronize, syncunlock;
    deque<DWORD> idqueue;
    set<DWORD> current;

public:

    ownsemaphore(int cap){
        capacity=cap;
        synchronize=false;
        syncunlock=false;
    }

    void Lock(){
        while(synchronize);
        InterlockedIncrement(&synchronize);
        if(current.find(GetCurrentThreadId())!=current.end()){
            idqueue.push_back(GetCurrentThreadId());
            while(current.size()>=capacity||idqueue.front()!=GetCurrentThreadId())
                Sleep(10);
            current.insert(idqueue.front());
            idqueue.pop_front();
        }
        InterlockedDecrement(&synchronize);
    }

    void Unlock(){
        while(syncunlock);
        InterlockedIncrement(&syncunlock);
        set<DWORD>::iterator it=current.find(GetCurrentThreadId());
        if(it!=current.end())
            current.erase(it);
        InterlockedDecrement(&syncunlock);
    }

};

#endif // OWNSEMAPHORE_H_INCLUDED
