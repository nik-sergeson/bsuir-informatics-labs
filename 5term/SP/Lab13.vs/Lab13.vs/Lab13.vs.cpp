// Lab13.vs.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "Lab13.vs.h"
#include <string>
#include <tchar.h>
#include <iostream>
#include <windows.h>
#include <tlhelp32.h>
#include <stdio.h>
#include <vector>
#include "Resource.h"
#include <psapi.h>
#include <windowsx.h>
#include <winbase.h>

std::vector<DWORD> processid;
#define MAX_LOADSTRING 100

// Global Variables:
HINSTANCE hInst;								// current instance
TCHAR szTitle[MAX_LOADSTRING];					// The title bar text
TCHAR szWindowClass[MAX_LOADSTRING];			// the main window class name

// Forward declarations of functions included in this code module:
ATOM				MyRegisterClass(HINSTANCE hInstance);
BOOL				InitInstance(HINSTANCE, int);
LRESULT CALLBACK	WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK	About(HWND, UINT, WPARAM, LPARAM);

int APIENTRY _tWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPTSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
	UNREFERENCED_PARAMETER(hPrevInstance);
	UNREFERENCED_PARAMETER(lpCmdLine);

 	// TODO: Place code here.
	MSG msg;
	HACCEL hAccelTable;

	// Initialize global strings
	LoadString(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
	LoadString(hInstance, IDC_LAB13VS, szWindowClass, MAX_LOADSTRING);
	MyRegisterClass(hInstance);

	// Perform application initialization:
	if (!InitInstance (hInstance, nCmdShow))
	{
		return FALSE;
	}

	hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_LAB13VS));

	// Main message loop:
	while (GetMessage(&msg, NULL, 0, 0))
	{
		if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
	}

	return (int) msg.wParam;
}



//
//  FUNCTION: MyRegisterClass()
//
//  PURPOSE: Registers the window class.
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
	WNDCLASSEX wcex;

	wcex.cbSize = sizeof(WNDCLASSEX);

	wcex.style			= CS_HREDRAW | CS_VREDRAW;
	wcex.lpfnWndProc	= WndProc;
	wcex.cbClsExtra		= 0;
	wcex.cbWndExtra		= 0;
	wcex.hInstance		= hInstance;
	wcex.hIcon			= LoadIcon(hInstance, MAKEINTRESOURCE(IDI_LAB13VS));
	wcex.hCursor		= LoadCursor(NULL, IDC_ARROW);
	wcex.hbrBackground	= (HBRUSH)(COLOR_WINDOW+1);
	wcex.lpszMenuName	= NULL;
	wcex.lpszClassName	= szWindowClass;
	wcex.hIconSm		= LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

	return RegisterClassEx(&wcex);
}

//
//   FUNCTION: InitInstance(HINSTANCE, int)
//
//   PURPOSE: Saves instance handle and creates main window
//
//   COMMENTS:
//
//        In this function, we save the instance handle in a global variable and
//        create and display the main program window.
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   HWND hWnd;

   hInst = hInstance; // Store instance handle in our global variable

   hWnd = CreateWindow(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT, 0, 644, 375, NULL, NULL, hInstance, NULL);

   if (!hWnd)
   {
      return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

//
//  FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  PURPOSE:  Processes messages for the main window.
//
//  WM_COMMAND	- process the application menu
//  WM_PAINT	- Paint the main window
//  WM_DESTROY	- post a quit message and return
//
//

void GetModuleList(HWND hwnd,int id){
 bool exists = false;
    MODULEENTRY32 entry;
    entry.dwSize = sizeof(MODULEENTRY32);
    HANDLE const snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, processid[id]);
    Module32First(snapshot, &entry);
    if( !Module32First( snapshot, &entry ) )
      {
        std::wstring str=L"64bit procces, cannot load modules";
        SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_ADDSTRING, 0, (LPARAM)str.c_str());
        CloseHandle( snapshot );     // Must clean up the snapshot object!
        return;
      }
        do{
                std::wstring str;
                str=entry.szModule;
                SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_ADDSTRING, 0, (LPARAM)str.c_str());
				SendDlgItemMessage(hwnd, ID_SECONDBOX, LB_SETHORIZONTALEXTENT, 8*str.length(),NULL);
        }while (Module32Next(snapshot, &entry));
    CloseHandle(snapshot);
}

void GetProcessList(HWND hwnd)
{
    bool exists = false;
    PROCESSENTRY32 entry;
    entry.dwSize = sizeof(PROCESSENTRY32);

    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

    if (Process32First(snapshot, &entry))
        while (Process32Next(snapshot, &entry)){
                char *num=(char *)calloc(2,sizeof(char));
                HANDLE  hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, entry.th32ProcessID );
                int dwPriorityClass = GetPriorityClass( hProcess );
                CloseHandle(hProcess);
				std::wstring wstr;
				wstr=entry.szExeFile;
				wstr+=L",priority: ";
				wstr+=std::to_wstring(dwPriorityClass);
                processid.push_back(entry.th32ProcessID);
				SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_ADDSTRING, 0, (LPARAM)wstr.c_str());
				SendDlgItemMessage(hwnd, ID_FIRSTTBOX, LB_SETHORIZONTALEXTENT, 8*wstr.length(),NULL);
        }
    CloseHandle(snapshot);
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	int wmId, wmEvent;
	PAINTSTRUCT ps;
	HDC hdc;
	HWND hListBox=NULL;
	switch (message)
	{
		case WM_CREATE:
        {
			hListBox = CreateWindowEx(WS_EX_CLIENTEDGE,L"LISTBOX", NULL, WS_HSCROLL|LBS_NOTIFY|WS_VSCROLL|WS_CHILD|WS_VISIBLE, 10, 45, 300, 200, hWnd, (HMENU)ID_FIRSTTBOX, GetModuleHandle(NULL), NULL);
			HWND hListBox2 = CreateWindowEx(WS_EX_CLIENTEDGE,L"LISTBOX", NULL, WS_VSCROLL|WS_HSCROLL|WS_CHILD | WS_VISIBLE | ES_AUTOVSCROLL, 320, 45, 300, 200, hWnd, (HMENU)ID_SECONDBOX, GetModuleHandle(NULL), NULL);
		
			GetProcessList(hWnd);
		}
	case WM_COMMAND:
		{
            switch(LOWORD(wParam))
            {
                case ID_FIRSTTBOX:
                {
                    switch(HIWORD(wParam))
                    {
                        case LBN_SELCHANGE:
                            {
								HWND hList = GetDlgItem(hWnd, ID_FIRSTTBOX);
                                int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
                                SendDlgItemMessage(hWnd, ID_SECONDBOX, LB_RESETCONTENT,NULL,NULL);
                                GetModuleList(hWnd,lcount);
                            }
                        break;
                        case LBN_DBLCLK:
                            {
                                HMENU hPopupMenu = LoadMenu(NULL,MAKEINTRESOURCE(ID_MENU));
                                hPopupMenu=GetSubMenu(hPopupMenu,0);
                                POINT pt;
                                GetCursorPos(&pt);
                                int nind=TrackPopupMenu(hPopupMenu,TPM_LEFTALIGN,pt.x,pt.y,0,hWnd,0);
                            }
                            break;
                    }
                }
                break;
                case ID_IDLE:
                {
					HWND hList = GetDlgItem(hWnd, ID_FIRSTTBOX);
                    int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
                    HANDLE hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, processid[lcount] );
					SetPriorityClass(hProcess,IDLE_PRIORITY_CLASS);
                    CloseHandle(hProcess);
                    SendDlgItemMessage(hWnd, ID_FIRSTTBOX, LB_RESETCONTENT,NULL,NULL);
					GetProcessList(hWnd);

                }
                break;
				case ID_NORMAL:
					{
						HWND hList = GetDlgItem(hWnd, ID_FIRSTTBOX);
						int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
						HANDLE hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, processid[lcount] );
						SetPriorityClass(hProcess,NORMAL_PRIORITY_CLASS);
						CloseHandle(hProcess);
						SendDlgItemMessage(hWnd, ID_FIRSTTBOX, LB_RESETCONTENT,NULL,NULL);
						GetProcessList(hWnd);
					}
				break;
				case ID_HIGH:
					{
						HWND hList = GetDlgItem(hWnd, ID_FIRSTTBOX);
						int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
						HANDLE hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, processid[lcount] );
						SetPriorityClass(hProcess,HIGH_PRIORITY_CLASS);
						CloseHandle(hProcess);
						SendDlgItemMessage(hWnd, ID_FIRSTTBOX, LB_RESETCONTENT,NULL,NULL);
						GetProcessList(hWnd);
					}
				break;
				case ID_REALTIME:
					{
						HWND hList = GetDlgItem(hWnd, ID_FIRSTTBOX);
						int lcount = SendMessage(hList, LB_GETCURSEL, 0, 0);
						HANDLE hProcess = OpenProcess( PROCESS_ALL_ACCESS, FALSE, processid[lcount] );
						SetPriorityClass(hProcess,REALTIME_PRIORITY_CLASS);
						CloseHandle(hProcess);
						SendDlgItemMessage(hWnd, ID_FIRSTTBOX, LB_RESETCONTENT,NULL,NULL);
						GetProcessList(hWnd);
					}
				break;
            }
        }
        break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd, message, wParam, lParam);
	}
	return 0;
}

// Message handler for about box.
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
	UNREFERENCED_PARAMETER(lParam);
	switch (message)
	{
	case WM_INITDIALOG:
		return (INT_PTR)TRUE;

	case WM_COMMAND:
		if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
		{
			EndDialog(hDlg, LOWORD(wParam));
			return (INT_PTR)TRUE;
		}
		break;
	}
	return (INT_PTR)FALSE;
}
