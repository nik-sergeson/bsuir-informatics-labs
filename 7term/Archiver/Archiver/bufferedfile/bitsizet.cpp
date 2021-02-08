#include "bitsizet.h"

bit_size_t* CreateBitSize(long int size_byte, char tail_size){
    bit_size_t *file_size=(bit_size_t *)malloc(sizeof(bit_size_t));
    file_size->tail_size_bit=tail_size;
    file_size->size_byte=size_byte;
    return file_size;
}

bit_size_t* CreateBitSize(){
    bit_size_t *file_size=(bit_size_t *)malloc(sizeof(bit_size_t));
    file_size->tail_size_bit=0;
    file_size->size_byte=0;
    return file_size;
}

void FreeBitSize(bit_size_t *size){
    free(size);
}

bit_size_t Substract(const file_position_t& first, const file_position_t& second){
    bit_size_t result;
    if(first.byte_position>second.byte_position || ((first.byte_position==second.byte_position)&&(first.bit_position>=second.bit_position))){
        result.size_byte=first.byte_position-second.byte_position;
        if(first.bit_position<second.bit_position){
            --result.size_byte;
            result.tail_size_bit=BYTE_SIZE_BITS+first.bit_position-second.bit_position;
        }
        else
            result.tail_size_bit=first.bit_position-second.bit_position;
    }
    else{
        result.size_byte=second.byte_position-first.byte_position;
        if(second.bit_position<first.bit_position){
            --result.size_byte;
            result.tail_size_bit=BYTE_SIZE_BITS+second.bit_position-first.bit_position;
        }
        else
            result.tail_size_bit=second.bit_position-first.bit_position;
    }
    return result;
}

file_position_t Add(const file_position_t& position, const bit_size_t& offset){
    file_position_t new_position=position;
    new_position.byte_position+=offset.size_byte;
    if(new_position.bit_position+offset.tail_size_bit>=BYTE_SIZE_BITS){
        ++new_position.byte_position;
        new_position.bit_position+=offset.tail_size_bit-BYTE_SIZE_BITS;
    }
    else
        new_position.bit_position+=offset.tail_size_bit;
    return new_position;
}
