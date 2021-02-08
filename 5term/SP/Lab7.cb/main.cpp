#if defined(UNICODE) && !defined(_UNICODE)
    #define _UNICODE
#elif defined(_UNICODE) && !defined(UNICODE)
    #define UNICODE
#endif

#include <tchar.h>
#include <windows.h>
#include <iostream>
#include "Resource.h"

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
           644,                 /* The programs width */
           475,                 /* and height in pixels */
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
            {
                HWND hWndButton1=CreateWindowEx(NULL, "BUTTON","Add",WS_VISIBLE|WS_CHILD,10,255,100,24,hwnd,(HMENU)ID_ADDBUTTON,GetModuleHandle(NULL),NULL);
                HWND hWndButton2=CreateWindowEx(NULL, "BUTTON","To Right",WS_VISIBLE|WS_CHILD,210,255,100,24,hwnd,(HMENU)ID_TORIGHTBUTTON,GetModuleHandle(NULL),NULL);
                HWND hWndButton3=CreateWindowEx(NULL, "BUTTON","Clear",WS_VISIBLE|WS_CHILD,320,255,100,24,hwnd,(HMENU)ID_CLEARBUTTON,GetModuleHandle(NULL),NULL);
                HWND hWndButton4=CreateWindowEx(NULL, "BUTTON","Delete",WS_VISIBLE|WS_CHILD,520,255,100,24,hwnd,(HMENU)ID_DELETEBUTTON,GetModuleHandle(NULL),NULL);
                HWND hEdit=CreateWindowEx(WS_EX_CLIENTEDGE,"EDIT","",WS_CHILD|WS_VISIBLE|ES_AUTOHSCROLL,10,10,300,25,hwnd,(HMENU)ID_EDIT,GetModuleHandle(NULL),NULL);
                HWND hListBox = CreateWindowEx(NULL,"LISTBOX", NULL, WS_HSCROLL|WS_VSCROLL|WS_CHILD|WS_VISIBLE, 10, 45, 300, 200, hwnd, (HMENU)ID_FIRSTTBOX, GetModuleHandle(NULL), NULL);
                //SendMessage(hListBox,LB_SETHORIZONTALEXTENT,1000,0);
                HWND hListBox2 = CreateWindowEx(WS_EX_CLIENTEDGE,"LISTBOX", NULL, WS_VSCROLL|WS_HSCROLL|WS_CHILD | WS_VISIBLE | ES_AUTOVSCROLL, 320, 45, 300, 200, hwnd, (HMENU)ID_SECONDBOX, GetModuleHandle(NULL), NULL);
            }
            break;
        case WM_COMMAND:
            {
                switch(LOWORD(wParam))
                {
                    case ID_ADDBUTTON:
                        {
                            int len = GetWindowTextLength(GetDlgItem(hwnd, ID_EDIT));
                            if(len>0){
                                char* buf=(char*)calloc(len+1,sizeof(char));
                                GetDlgItemText(hwnd,ID_EDIT, buf, len + 1);
                                HWND hList = GetDlgItem(hwnd, ID_FIRSTTBOX);
                                int lindex=SendMessage(hList, LB_FINDSTRING, -1, (LPARAM)buf);
                                if(lindex==-1){
                                    SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_ADDSTRING, 0, (LPARAM)buf);
                                    SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_SETHORIZONTALEXTENT, 8*strlen(buf),NULL);
                                    }
                                else
                                    free(buf);
                                SetDlgItemText(hwnd, ID_EDIT, "");
                            }
                        }
                        break;
                    case ID_CLEARBUTTON:
                        {
                            HWND hList = GetDlgItem(hwnd, ID_FIRSTTBOX);
                            SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_RESETCONTENT, NULL,NULL);
                            HWND hList2 = GetDlgItem(hwnd, ID_SECONDBOX);
                            SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_RESETCONTENT,NULL,NULL);
                            SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_SETHORIZONTALEXTENT, 0,NULL);
                            SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_SETHORIZONTALEXTENT, 0,NULL);
                        }
                        break;
                    case ID_TORIGHTBUTTON:
                        {
                            HWND hList = GetDlgItem(hwnd, ID_FIRSTTBOX);
                            int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
                            int len=SendMessage(hList, LB_GETTEXTLEN, (WPARAM)lcount, 0);
                            char* buf=(char*)calloc(len+1,sizeof(char));
                            SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_GETTEXT, lcount, (LPARAM)buf);
                            hList = GetDlgItem(hwnd, ID_SECONDBOX);
                            int lindex=SendMessage(hList, LB_FINDSTRING, -1, (LPARAM)buf);
                            if(lindex==-1){
                                SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_ADDSTRING, 0, (LPARAM)buf);
                                SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_SETHORIZONTALEXTENT, 8*strlen(buf),NULL);
                            }
                            else
                                free(buf);
                        }
                        break;
                    case ID_DELETEBUTTON:
                        {
                            HWND hList1 = GetDlgItem(hwnd, ID_FIRSTTBOX);
                            HWND hList2 = GetDlgItem(hwnd, ID_SECONDBOX);
                            int index1 = SendMessage(hList1, LB_GETCURSEL, 0, 0),index2=SendMessage(hList2, LB_GETCURSEL, 0, 0);
                            if(index1!=-1){
                                 SendMessage(hList1, LB_DELETESTRING, index1, NULL);
                                 SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_SETHORIZONTALEXTENT, 0,NULL);
                            }
                            if(index2!=-1){
                                SendMessage(hList2, LB_DELETESTRING, index2,NULL);
                                SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_SETHORIZONTALEXTENT, 0,NULL);
                            }
                        }
                        break;
                }
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
