#ifndef HUFFMANCODE_H_INCLUDED
#define HUFFMANCODE_H_INCLUDED
#include <stdlib.h>

#define MAX_CODE_LENGTH 64
#define LS_BYTE_MASK 0xFF

class HuffmanCode{
public:
    HuffmanCode();
    HuffmanCode(const HuffmanCode* h_code);
    void AddBit(int bit);
    void ShiftRight(int bit_count);
    int bits() const;
    int length() const;
    void setbits(long long bits, int length);
    void Update(const HuffmanCode* h_code);
private:
    long long int bits_;
    int length_;
};
#endif // HUFFMANCODE_H_INCLUDED
