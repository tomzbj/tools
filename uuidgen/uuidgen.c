// Generate a uuid.  
#include <windows.h>
#include <stdio.h>

int main(void)
{
    GUID guid;

    CoInitializeEx(NULL, COINIT_SPEED_OVER_MEMORY);
    CoCreateGuid(&guid);

    printf("%08lx-%04x-%04x-%02x%02x%02x%02x%02x%02x%02x%02x\n", 
            guid.Data1, guid.Data2, guid.Data3, guid.Data4[0], guid.Data4[1], 
            guid.Data4[2], guid.Data4[3], guid.Data4[4], guid.Data4[5], 
            guid.Data4[6], guid.Data4[7] );

    return 0;
}
