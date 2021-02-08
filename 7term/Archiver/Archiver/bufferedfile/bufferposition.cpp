#include "bufferposition.h"

buffer_position_t* CreateBufferPosition(long int byte_position, char bit_position, long int block_size){
    buffer_position_t *buffer_posittion=(buffer_position_t *)malloc(sizeof(buffer_position_t));
    buffer_posittion->byte_position=byte_position;
    buffer_posittion->bit_position=bit_position;
    buffer_posittion->max_block_size=block_size;
    return buffer_posittion;
}

buffer_position_t* CreateBufferPosition(long int block_size){
    buffer_position_t *file_posittion=(buffer_position_t *)malloc(sizeof(buffer_position_t));
    file_posittion->byte_position=0;
    file_posittion->bit_position=0;
    file_posittion->max_block_size=block_size;
    return file_posittion;
}


void FreeBufferPosition(buffer_position_t *position){
    free(position);
}


