#if defined(UNICODE) && !defined(_UNICODE)
    #define _UNICODE
#elif defined(_UNICODE) && !defined(UNICODE)
    #define UNICODE
#endif

#include <tchar.h>
#include <windows.h>
#include "resource.h"
#include <iostream>

const int ID_TIMER=10;

typedef struct Text{
long x,y,speed;
bool start=false;
LPCSTR message="My Test Message";

Text(){
x=y=0;
speed=-10;
}

void Draw(HWND hwnd){
    RECT position;
    HDC wdc = GetWindowDC(hwnd);
    GetClientRect (hwnd, &position) ;
    SetBkMode(wdc,TRANSPARENT);
    position.left=-position.right;
    if(x-strlen(message)*9+speed+position.right>2*position.right||x+strlen(message)*9+speed+position.right>2*position.right)
       speed=-speed;
    x+=speed;
    position.left=x;
    position.top=y;
    DrawText (wdc,message, -1, &position, DT_SINGLELINE | DT_VCENTER | DT_CENTER);
    ReleaseDC (hwnd, wdc);
}

};

Text mymess;
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
    wincl.hIcon = (HICON)LoadImage(NULL,"pacman.ico",IMAGE_ICON,32,32,LR_LOADFROMFILE);
    wincl.hIconSm =LoadIcon(hThisInstance,MAKEINTRESOURCE(ID_ICON));
    wincl.hCursor = LoadCursor(hThisInstance,MAKEINTRESOURCE(ID_CURSOR));
    wincl.lpszMenuName = MAKEINTRESOURCE(IDR_MYMENU);                /* No menu */
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


/*  This function is called by the Windows function DispatchMessage()  */

LRESULT CALLBACK WindowProcedure (HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)                  /* handle the messages */
    {
        case WM_CREATE:
            break;
        case WM_DESTROY:
            PostQuitMessage (0);       /* send a WM_QUIT to the message queue */
            break;
        case WM_TIMER:
            InvalidateRect(hwnd,NULL,true);
            break;
        case WM_PAINT:
            {
            PAINTSTRUCT ps;
            HDC hdc=BeginPaint(hwnd,&ps);
            if(mymess.start)
                mymess.Draw(hwnd);
            EndPaint(hwnd,&ps);
            }
            break;
        case WM_COMMAND:
            switch(LOWORD(wParam))
            {
                case ID_START:
                    {
                     SetTimer(hwnd,ID_TIMER,100,(TIMERPROC) NULL);
                     mymess.start=true;
                    }
                break;
                case ID_STOP:
                    KillTimer(hwnd,ID_TIMER);
                break;
            }
        break;
        default:                      /* for messages that we don't deal with */
            return DefWindowProc (hwnd, message, wParam, lParam);
    }

    return 0;
}
