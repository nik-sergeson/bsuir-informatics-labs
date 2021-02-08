#ifndef BITSIZET
#define BITSIZET
#include <cstdlib>
#include "../fileutils/fileposition.h"

#define BYTE_SIZE_BITS 8

typedef struct{
    long int size_byte;
    char tail_size_bit;
}bit_size_t;

bit_size_t* CreateBitSize(long int size_byte, char tail_size);
bit_size_t* CreateBitSize();
bit_size_t Substract(const file_position_t& first, const file_position_t& second);
file_position_t Add(const file_position_t& position, const bit_size_t& offset);
void FreeBitSize(bit_size_t *size);

#endif // BITSIZET

