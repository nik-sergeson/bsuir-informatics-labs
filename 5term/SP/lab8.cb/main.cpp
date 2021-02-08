#if defined(UNICODE) && !defined(_UNICODE)
    #define _UNICODE
#elif defined(_UNICODE) && !defined(UNICODE)
    #define UNICODE
#endif

#include <tchar.h>
#include <windows.h>
#include <iostream>
#include "resource.h"

bool ShipVisible;

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
    wincl.lpszMenuName = NULL;                 /* No menu */
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
           744,                 /* The programs width */
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

void DrawShip(HDC hDC,PAINTSTRUCT Ps){
    POINT Pt[30];
	DWORD  lpPts[] = { 16,4,10 };
	Pt[0].x = 100;
	Pt[0].y = 300;
	Pt[1].x = 30;
	Pt[1].y = 300;
	Pt[2].x = 90;
	Pt[2].y = 260;
	Pt[3].x = 90;
	Pt[3].y = 250;
	Pt[4].x =  100;
	Pt[4].y =  250;
	Pt[5].x = 100;
	Pt[5].y =  245;
	Pt[6].x = 90;
	Pt[6].y =  245;
	Pt[7].x =  90;
	Pt[7].y =  205;
	Pt[8].x  = 100;
	Pt[8].y  =  195;
	Pt[9].x  = 100;
	Pt[9].y  =  160;
	Pt[10].x = 110;
	Pt[10].y =  160;
	Pt[11].x = 110;
	Pt[11].y =  130;
	Pt[12].x = 130;
	Pt[12].y =  130;
	Pt[13].x = 130;
	Pt[13].y =  160;
	Pt[14].x = 140;
	Pt[14].y = 160;
	Pt[15].x = 140;
	Pt[15].y = 130;
	Pt[16].x = 160;
	Pt[16].y = 130;
	Pt[17].x = 160;
	Pt[17].y = 160;
	Pt[18].x = 170;
	Pt[18].y = 160;
	Pt[19].x = 170;
	Pt[19].y = 130;
	Pt[20].x = 190;
	Pt[20].y = 130;
	Pt[21].x = 190;
	Pt[21].y = 160;
	Pt[22].x = 230;
	Pt[22].y = 160;
	Pt[23].x = 230;
	Pt[23].y = 110;
	Pt[24].x = 350;
	Pt[24].y = 110;
	Pt[25].x = 350;
	Pt[25].y = 120;
	Pt[26].x = 330;
	Pt[26].y = 120;
	Pt[27].x = 330;
	Pt[27].y = 160;
	Pt[28].x = 330;
	Pt[28].y = 270;
	Pt[29].x = 318;
	Pt[29].y = 270;
	PolyPolyline(hDC, Pt, lpPts, 3);
	Rectangle(hDC,640,270,380,180);
	Ellipse(hDC,90,260,140,310);
	Ellipse(hDC,150,260,200,310);
    Ellipse(hDC,230,220,320,310);
    Ellipse(hDC,380,270,420,310);
    Ellipse(hDC,600,270,640,310);
    Ellipse(hDC,550,270,590,310);
    Rectangle(hDC,130,275,285,285);
    Rectangle(hDC,640,270,380,180);
    Rectangle(hDC,240,130,260,160);
    Rectangle(hDC,270,130,320,160);
    MoveToEx(hDC,135,280,NULL);
    LineTo(hDC,280,280);
    MoveToEx(hDC,330,260,NULL);
    LineTo(hDC,380,260);
    Arc(hDC,140,120,161,140,161,133,140,133);
    Arc(hDC,170,120,191,140,191,133,170,133);
}

/*  This function is called by the Windows function DispatchMessage()  */

LRESULT CALLBACK WindowProcedure (HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)                  /* handle the messages */
    {
        case WM_CREATE:
            {
                HWND hWndButton1=CreateWindowEx(NULL, "BUTTON","Draw",WS_VISIBLE|WS_CHILD|BS_OWNERDRAW,150,20,100,24,hwnd,(HMENU)ID_DRAWBUTTON,GetModuleHandle(NULL),NULL);
                HWND hWndButton2=CreateWindowEx(NULL, "BUTTON","CLear",WS_VISIBLE|WS_CHILD|BS_OWNERDRAW,300,20,100,24,hwnd,(HMENU)ID_CLEARBUTTON,GetModuleHandle(NULL),NULL);
                ShipVisible=false;
            }
            break;
        case WM_PAINT:
            {
                RECT position;
                GetClientRect (hwnd, &position) ;
                PAINTSTRUCT Ps;
                HDC hDC = BeginPaint(hwnd, &Ps);
                FillRect(hDC, &position,(HBRUSH) GetStockObject(WHITE_BRUSH));
                if(ShipVisible)
                    DrawShip(hDC,Ps);
                EndPaint(hwnd, &Ps);
            }
            break;
        case WM_DRAWITEM:
            {
                HBRUSH NewBrush;
                LPDRAWITEMSTRUCT pdis =(LPDRAWITEMSTRUCT) lParam;
                SetBkMode(pdis->hDC,TRANSPARENT);
                FillRect(pdis->hDC, &pdis->rcItem,(HBRUSH) GetStockObject(WHITE_BRUSH));
                switch(pdis->CtlID){
                    case ID_DRAWBUTTON:
                        NewBrush = CreateSolidBrush(RGB(0, 255,0));
                        break;
                    case ID_CLEARBUTTON:
                        NewBrush = CreateSolidBrush(RGB(255, 0, 0));
                        break;
                }
                SelectObject(pdis->hDC, NewBrush);
                Ellipse(pdis->hDC,pdis->rcItem.left,pdis->rcItem.top,pdis->rcItem.right,pdis->rcItem.bottom);
                DeleteObject(NewBrush);
                switch(pdis->CtlID){
                    case ID_DRAWBUTTON:
                        DrawText (pdis->hDC,"Draw", -1, &pdis->rcItem, DT_SINGLELINE | DT_VCENTER | DT_CENTER);
                        break;
                    case ID_CLEARBUTTON:
                        DrawText (pdis->hDC,"Clear", -1, &pdis->rcItem, DT_SINGLELINE | DT_VCENTER | DT_CENTER);
                        break;
                }
                if(pdis->itemState & ODS_FOCUS){
                    DrawFocusRect(pdis->hDC,&pdis->rcItem);
                }
            }
            break;
        case WM_COMMAND:
            {
                switch(LOWORD(wParam)){
                case ID_DRAWBUTTON:
                    {
                        ShipVisible=true;
                    }
                    break;
                case ID_CLEARBUTTON:
                    {
                        ShipVisible=false;
                    }
                    break;
                }
                InvalidateRect(hwnd,NULL,NULL);
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
