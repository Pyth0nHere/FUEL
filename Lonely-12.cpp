#include <windows.h>
#include <tlhelp32.h>
#include <tchar.h>

using namespace std;

bool process_is_running(const TCHAR* const executableName)
{
    PROCESSENTRY32 entry;
    entry.dwSize = sizeof(PROCESSENTRY32);

    const auto snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    if (!Process32First(snapshot, &entry))
    {
        CloseHandle(snapshot);
        return false;
    }

    do
    {
        if (!_tcsicmp(entry.szExeFile, executableName))
        {
            CloseHandle(snapshot);
            return true;
        }
    } while (Process32Next(snapshot, &entry));

    CloseHandle(snapshot);

    return false;
}

int main()
{
    while (true)
    {
        if (process_is_running("Format-22.pyw") == false)
        {
            system("Eradication-Typhoon.pyw");
            break;
        }
    }
}