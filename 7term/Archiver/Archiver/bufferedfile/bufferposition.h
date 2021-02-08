#ifndef BUFFERPOSITION
#define BUFFERPOSITION
#include <cstdlib>

typedef struct{
    long int byte_position;
    char bit_position;
    long int max_block_size;
}buffer_position_t;

buffer_position_t* CreateBufferPosition(long int byte_position, char bit_position, long int block_size);
buffer_position_t* CreateBufferPosition(long int block_size);
void FreeBufferPosition(buffer_position_t *position);

#endif // BUFFERPOSITION

