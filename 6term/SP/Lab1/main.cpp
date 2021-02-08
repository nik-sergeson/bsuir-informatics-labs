#include <iostream>
#include <set>
#include <deque>
#include <stdio.h>
#include <windows.h>
#include "ownsemaphore.h"
#include "OwnMutex.h"
#include <process.h>
#include <ctime>
using namespace std;

ownmutex lock_mutex;
ownsemaphore losk_semaphore(10);
HANDLE ghMutex;

void function1(LPVOID params){
    lock_mutex.Lock();
    printf("Function 1 starts\n");
    Sleep(3000);
    printf("Function 1 ends\n");
    lock_mutex.Unlock();
}

void function2(LPVOID params){
    lock_mutex.Lock();
    printf("Function 2 starts\n");
    printf("Function 2 ends\n");
    lock_mutex.Unlock();
}

void function3(LPVOID params){
    lock_mutex.Lock();
    lock_mutex.Lock();
    lock_mutex.Unlock();
    printf("Still alive\n");
}

void function4(LPVOID params){
    lock_mutex.Lock();
    Sleep(3000);
    lock_mutex.Unlock();
    printf("Function4 end\n");
}

void function5(LPVOID params){
    printf("Trying relock mutex\n");
    lock_mutex.Unlock();
    lock_mutex.Lock();
    printf("Mutex is mine\n");
    lock_mutex.Unlock();
}

void standartmutextest(){
    printf("------Standart mutex--------\n");
    clock_t start, endt;
    start = clock();
    WaitForSingleObject(ghMutex, INFINITE);
    endt = clock();
    cout<<"Time for lock "<<(endt-start)<<" milliSeconds"<<endl;
    start = clock();
    ReleaseMutex(ghMutex);
    endt = clock();
    cout<<"Time for unlock "<<(endt-start)<<" milliSeconds"<<endl;
}

void ownmutextest(){
    printf("------Own mutex--------\n");
    clock_t start, endt;
    start = clock();
    lock_mutex.Lock();
    endt = clock();
    cout<<"Time for lock "<<(endt-start)<<" milliSeconds"<<endl;
    start = clock();
    lock_mutex.Unlock();
    endt= clock();
    cout<<"Time for unlock "<<(endt-start)<<" milliSeconds"<<endl;
}

int main()
{
    _beginthread(function1,0,NULL);
    _beginthread(function2,0,NULL);
    _beginthread(function3,0,NULL);
    Sleep(4000);
     _beginthread(function4,0,NULL);
    _beginthread(function5,0,NULL);
    Sleep(5000);
    ghMutex = CreateMutex( NULL, FALSE, NULL);
    standartmutextest();
    ownmutextest();
    while(true);
    return 0;
}
