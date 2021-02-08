#ifndef FILEPOSITION
#define FILEPOSITION
#include <cstdlib>

#define BYTE_SIZE_BITS 8

typedef struct{
    long int byte_position;
    char bit_position;
}file_position_t;

file_position_t* CreateFilePosition(long int byte_position, char bit_position);
file_position_t* CreateFilePosition();
void FreeFilePosition(file_position_t *position);

#endif // FILEPOSITION

