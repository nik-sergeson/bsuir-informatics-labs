#include "huffmancode.h"

void HuffmanCode::ShiftRight(int bit_count){
    if(bit_count >= length_){
        bits_=0;
        length_=0;
    }
    else{
        bits_ >>= bit_count;
        length_ -= bit_count;
    }
}

void HuffmanCode::AddBit(int bit){
    bits_ <<= 1;
    if(bit)
        bits_ |= 1;
    ++length_;
}

int HuffmanCode::bits() const{
    return bits_;
}

int HuffmanCode::length()const {
    return length_;
}

HuffmanCode::HuffmanCode(){
    bits_=0;
    length_=0;
}


HuffmanCode::HuffmanCode(const HuffmanCode* h_code){
    bits_=h_code->bits();
    length_=h_code->length();
}

void HuffmanCode::setbits(long long bits, int length){
    bits_=bits;
    length_=length;
}

void HuffmanCode::Update(const HuffmanCode *h_code){
    bits_=h_code->bits();
    length_=h_code->length();
}

