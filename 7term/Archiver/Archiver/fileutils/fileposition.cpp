#include "fileposition.h"

file_position_t* CreateFilePosition(long int byte_position, char bit_position){
    file_position_t *file_position=(file_position_t *)malloc(sizeof(file_position_t));
    file_position->byte_position=byte_position;
    file_position->bit_position=bit_position;
    return file_position;
}

file_position_t* CreateFilePosition(){
    file_position_t *file_position=(file_position_t *)malloc(sizeof(file_position_t));
    file_position->byte_position=0;
    file_position->bit_position=0;
    return file_position;
}

void FreeFilePosition(file_position_t *position){
    free(position);
}
