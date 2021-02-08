#include "bufferedinfile.h"
#include <stdlib.h>
#include <archiverexception.h>


BufferedInFile::BufferedInFile(const string& path):BufferedBitFile(path){
    fp_=fopen(path.c_str(), "rb");
    if(fp_==NULL)
        throw ArchiverException("Cant open archive for reading");
    buffer_start_position.bit_position=0;
    buffer_start_position.byte_position=0;
}

int BufferedInFile::GetBit(){
    int return_value, read_quantity;
    if(size_->size_byte==0 && size_->tail_size_bit==0){
        return -1;
    }
    if(size_->tail_size_bit>0)
        --size_->tail_size_bit;
    else{
        size_->tail_size_bit=BYTE_SIZE_BITS-1;
        --size_->size_byte;
    }
    return_value=buffer_[buffer_position_->byte_position] & MSB_MASK;
    buffer_[buffer_position_->byte_position] <<= 1;
    ++buffer_position_->bit_position;
    if(buffer_position_->bit_position >= buffer_position_->max_block_size){
        ++buffer_position_->byte_position;
        buffer_position_->bit_position=0;
        if(buffer_position_->byte_position>=MAX_BUFFER_SIZE){
            read_quantity=size_->size_byte;
            if(size_->tail_size_bit!=0)
                read_quantity+=1;
            buffer_start_position.byte_position+=buffer_position_->byte_position;
            buffer_start_position.bit_position=0;
            if(read_quantity>MAX_BUFFER_SIZE){
                if(fread(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_)!=MAX_BUFFER_SIZE)
                    throw ArchiverException("Unexpected end of archive");
            }
            else{
                if(fread(buffer_, sizeof(unsigned char), read_quantity, fp_)!=read_quantity)
                    throw ArchiverException("Unexpected end of archive");
            }
            buffer_position_->byte_position=0;
        }
    }
    return return_value;
}

void BufferedInFile::ReadBlock(const bit_size_t& size, const file_position_t& position){
    int read_quantity, read;
    file_position_t position_right=Add(position, size);
    buffer_start_position.byte_position=position.byte_position;
    buffer_start_position.bit_position=position.bit_position;
    size_->size_byte=size.size_byte;
    size_->tail_size_bit=size.tail_size_bit;
    fseek(fp_, position.byte_position, SEEK_SET);
    read_quantity=0;
    read_quantity+=position_right.byte_position-position.byte_position;
    if(position_right.bit_position!=0)
        ++read_quantity;
    if(read_quantity>MAX_BUFFER_SIZE){
        if(fread(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_)!=MAX_BUFFER_SIZE)
            throw ArchiverException("Unexpected end of archive");
    }
    else{
        if((read=fread(buffer_, sizeof(unsigned char), read_quantity, fp_))!=read_quantity)
            throw ArchiverException("Unexpected end of archive");
    }
    buffer_[0]<<=position.bit_position;
    buffer_position_->byte_position=0;
    buffer_position_->bit_position=position.bit_position;
}

void BufferedInFile::ReadBlock(){
    buffer_start_position.byte_position=ftell(fp_);
    buffer_start_position.bit_position=0;
    size_->size_byte=fread(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
    size_->tail_size_bit=0;
    buffer_position_->bit_position=0;
    buffer_position_->byte_position=0;
}

file_position_t BufferedInFile::CurrentPosition()const{
    file_position_t position;
    position.byte_position=buffer_start_position.byte_position+buffer_position_->byte_position;
    position.bit_position=buffer_position_->bit_position;
    return position;
}

void BufferedInFile::Close(){
    fclose(fp_);
    fp_=NULL;
    size_->size_byte=0;
    size_->tail_size_bit=0;
    buffer_position_->bit_position=0;
    buffer_position_->byte_position=0;
    buffer_start_position.bit_position=0;
    buffer_start_position.byte_position=0;
}

void BufferedInFile::Reopen(){
    fp_=fopen(os_path_.c_str(), "rb");
}

int BufferedInFile::GetByte(){
    int read_quantity,return_value=0;
    if(size_->size_byte==0){
        return -1;
    }
    if(buffer_position_->byte_position>=MAX_BUFFER_SIZE){
        read_quantity=size_->size_byte;
        if(read_quantity>MAX_BUFFER_SIZE){
            if(fread(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_)!=MAX_BUFFER_SIZE)
                throw ArchiverException("Unexpected end of archive");
        }
        else{
            if(fread(buffer_, sizeof(unsigned char), read_quantity, fp_)!=read_quantity)
                throw ArchiverException("Unexpected end of archive");
        }
        buffer_position_->byte_position=0;
        buffer_start_position.byte_position=ftell(fp_);
        buffer_start_position.bit_position=0;
    }
    --size_->size_byte;
    return_value|=buffer_[buffer_position_->byte_position];
    ++buffer_position_->byte_position;
    return return_value;
}
