#if defined(UNICODE) && !defined(_UNICODE)
    #define _UNICODE
#elif defined(_UNICODE) && !defined(UNICODE)
    #define UNICODE
#endif

#include <tchar.h>
#include <windows.h>
#include "Resource.h"
#include <process.h>
#include <cmath>
#include <iostream>

#define PI 3.14159265

CRITICAL_SECTION cs;

typedef struct Arrow{
    int x;
    int y;
    int linethikness;
    COLORREF linecolor;
    int angle;
    int sleeptime;
    int linewidth;
    bool kill;
    HWND hwnd;
    CRITICAL_SECTION *cs;
    bool sleep;
    Arrow(){}

   Arrow( int x,int y,int linethikness,COLORREF linecolor,int angle,int sleeptime,int linewidth,bool kill,HWND hwnd,CRITICAL_SECTION *cs){
    this->x=x;
    this->y=y;
    this->linethikness=linethikness;
    this->linecolor=linecolor;
    this->angle=angle;
    this->sleeptime=sleeptime;
    this->linewidth=linewidth;
    this->kill=kill;
    this->hwnd=hwnd;
    this->cs=cs;
    sleep=false;
   }
};

typedef struct Backgroud{
int x;
int y;
CRITICAL_SECTION *cs;
HWND hwnd;
bool kill;
bool sleep;

Backgroud(){}

Backgroud(int x,int y,CRITICAL_SECTION *cs,HWND hwnd){
this->x=x;
this->y=y;
this->cs=cs;
this->hwnd=hwnd;
kill=false;
sleep=false;
}

};

/*  Declare Windows procedure  */
LRESULT CALLBACK WindowProcedure (HWND, UINT, WPARAM, LPARAM);

/*  Make the class name into a global variable  */
TCHAR szClassName[ ] = _T("CodeBlocksWindowsApp");

int WINAPI WinMain (HINSTANCE hThisInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR lpszArgument,
                     int nCmdShow)
{
    HWND hwnd;               /* This is the handle for our window */
    MSG messages;            /* Here messages to the application are saved */
    WNDCLASSEX wincl;        /* Data structure for the windowclass */

    /* The Window structure */
    wincl.hInstance = hThisInstance;
    wincl.lpszClassName = szClassName;
    wincl.lpfnWndProc = WindowProcedure;      /* This function is called by windows */
    wincl.style = CS_DBLCLKS;                 /* Catch double-clicks */
    wincl.cbSize = sizeof (WNDCLASSEX);

    /* Use default icon and mouse-pointer */
    wincl.hIcon = LoadIcon (NULL, IDI_APPLICATION);
    wincl.hIconSm = LoadIcon (NULL, IDI_APPLICATION);
    wincl.hCursor = LoadCursor (NULL, IDC_ARROW);
    wincl.lpszMenuName = MAKEINTRESOURCE(IDR_MYMENU); ;                 /* No menu */
    wincl.cbClsExtra = 0;                      /* No extra bytes after the window class */
    wincl.cbWndExtra = 0;                      /* structure or the window instance */
    /* Use Windows's default colour as the background of the window */
    wincl.hbrBackground = (HBRUSH) COLOR_BACKGROUND;

    /* Register the window class, and if it fails quit the program */
    if (!RegisterClassEx (&wincl))
        return 0;

    /* The class is registered, let's create the program*/
    hwnd = CreateWindowEx (
           0,                   /* Extended possibilites for variation */
           szClassName,         /* Classname */
           _T("Code::Blocks Template Windows App"),       /* Title Text */
           WS_OVERLAPPEDWINDOW, /* default window */
           CW_USEDEFAULT,       /* Windows decides the position */
           CW_USEDEFAULT,       /* where the window ends up on the screen */
           544,                 /* The programs width */
           375,                 /* and height in pixels */
           HWND_DESKTOP,        /* The window is a child-window to desktop */
           NULL,                /* No menu */
           hThisInstance,       /* Program Instance handler */
           NULL                 /* No Window Creation data */
           );

    /* Make the window visible on the screen */
    ShowWindow (hwnd, nCmdShow);

    /* Run the message loop. It will run until GetMessage() returns 0 */
    while (GetMessage (&messages, NULL, 0, 0))
    {
        /* Translate virtual-key messages into character messages */
        TranslateMessage(&messages);
        /* Send message to WindowProcedure */
        DispatchMessage(&messages);
    }

    /* The program return-value is 0 - The value that PostQuitMessage() gave */
    return messages.wParam;
}

void ArrowDraw(LPVOID params){
    Arrow *arr;
    arr=(Arrow *)params;
    int time=0,angle=-90;
    PAINTSTRUCT ps;
    RECT position;
    HDC hdc;
    Sleep(15);
    while(!arr->kill){
        EnterCriticalSection(arr->cs);
        std::cout<<"ARR"<<std::endl;
        GetClientRect (arr->hwnd, &position) ;
        hdc = GetDC(arr->hwnd);
        HPEN linePen;
        linePen = CreatePen(PS_SOLID, arr->linethikness, arr->linecolor);
        HGDIOBJ prevObj = SelectObject(hdc, linePen);
        MoveToEx(hdc,arr->x,arr->y,NULL);
        LineTo(hdc, (int)(arr->x+arr->linewidth*cos(angle*PI/180)), (int)(arr->y+arr->linewidth*sin(angle*PI/180)));
        SelectObject(hdc, prevObj);
        DeleteObject(linePen);
        DeleteDC(hdc);
        time+=1000;
        if(time%arr->sleeptime==0)
            angle=(angle+arr->angle)%360;
        LeaveCriticalSection(arr->cs);
        Sleep(1000);
        while(arr->sleep)
            Sleep(1000);
    }
_endthread();
}

void BackgroudDraw(LPVOID params){
Backgroud *bckg;
bckg=(Backgroud *)params;
EnterCriticalSection(bckg->cs);
PAINTSTRUCT ps;
HDC hdc;
BITMAP bm;
RECT position;
HBITMAP hBitmap = LoadBitmap(GetModuleHandle(NULL), MAKEINTRESOURCE(ID_CLOCK));
bool inthread=true;
while(!bckg->kill){
    EnterCriticalSection(bckg->cs);
    std::cout<<"BCKG"<<std::endl;
    GetClientRect (bckg->hwnd, &position) ;
    hdc = GetDC(bckg->hwnd);
    FillRect(hdc, &position,(HBRUSH) GetStockObject(WHITE_BRUSH));
    HDC hdcMem = CreateCompatibleDC(hdc);
    HGDIOBJ hbmOld = SelectObject(hdcMem, hBitmap);
    GetObject(hBitmap, sizeof(bm), &bm);
    BitBlt(hdc, bckg->x, bckg->y, bm.bmWidth, bm.bmHeight, hdcMem, 0, 0, SRCCOPY);
    SelectObject(hdcMem, hbmOld);
    DeleteDC(hdcMem);
    DeleteDC(hdc);
    if(inthread){
        LeaveCriticalSection(bckg->cs);
        inthread=false;
    }
    LeaveCriticalSection(bckg->cs);
    Sleep(1000);
    while(bckg->sleep)
        Sleep(1000);
}
}
/*  This function is called by the Windows function DispatchMessage()  */

LRESULT CALLBACK WindowProcedure (HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    static Arrow shour(198,149,7,RGB(0,0,0),30,6000,50,false,hwnd,&cs),minute(198,149,4,RGB(0,0,0),6,6000,80,false,hwnd,&cs),second(198,149,4,RGB(255,0,0),6,1000,80,false,hwnd,&cs);
    static Backgroud bckg(50,0,&cs,hwnd);
    switch (message)                  /* handle the messages */
    {
        case WM_PAINT:
        {

        }
        break;
        case WM_CREATE:
        {
            InitializeCriticalSection(&cs);
            _beginthread(BackgroudDraw,0,&bckg);
            _beginthread(ArrowDraw,0,&shour);
            _beginthread(ArrowDraw,0,&minute);
            _beginthread(ArrowDraw,0,&second);
        }
            break;
        case WM_COMMAND:
            switch(LOWORD(wParam))
            {
                case ID_START:
                    {
                        bckg.sleep=false;
                        shour.sleep=false;
                        minute.sleep=false;
                        second.sleep=false;
                    }
                break;
                case ID_STOP:
                    {
                        bckg.sleep=true;
                        shour.sleep=true;
                        minute.sleep=true;
                        second.sleep=true;
                    }
                break;
            }
        break;
        case WM_DESTROY:
            PostQuitMessage (0);       /* send a WM_QUIT to the message queue */
            break;
        default:                      /* for messages that we don't deal with */
            return DefWindowProc (hwnd, message, wParam, lParam);
    }

    return 0;
}
