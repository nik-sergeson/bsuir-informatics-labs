#include "bufferedoutfile.h"
#include <stdlib.h>

BufferedOutFile::BufferedOutFile(const string& os_path):BufferedBitFile(os_path){
    fp_=fopen(os_path.c_str(), "wb");
    if(fp_==NULL)
        throw ArchiverException("Cant open archive for writing");
}

void BufferedOutFile::WriteCode(const HuffmanCode* code){
    unsigned char temp_buff=0;
    long long int left_bits=0, mask=0;
    int shift_count, length;
    if(buffer_position_->max_block_size-buffer_position_->bit_position >= code->length()){
        temp_buff=0;
        temp_buff |= code->bits();
        shift_count=(buffer_position_->max_block_size-buffer_position_->bit_position)-code->length();
        temp_buff <<= shift_count;
        buffer_[buffer_position_->byte_position] |= temp_buff;
        buffer_position_->bit_position += code->length();
        if(buffer_position_->bit_position>=BYTE_SIZE_BITS){
            ++buffer_position_->byte_position;
            buffer_position_->bit_position=0;
            if(buffer_position_->byte_position >= MAX_BUFFER_SIZE){
                fwrite(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
                for(int i=0;i<MAX_BUFFER_SIZE;i++)
                    buffer_[i]=0;
                buffer_position_->byte_position=0;
            }
        }
        if(size_->tail_size_bit+code->length()< BYTE_SIZE_BITS){
            size_->tail_size_bit+=code->length();
        }
        else{
            ++size_->size_byte;
            size_->tail_size_bit+=code->length()-BYTE_SIZE_BITS;
        }
    }
    else{
        if(size_->tail_size_bit+code->length()< BYTE_SIZE_BITS){
            size_->tail_size_bit+=code->length();
        }
        else{
            size_->size_byte+=1+(code->length()-(buffer_position_->max_block_size-buffer_position_->bit_position))/BYTE_SIZE_BITS;
            size_->tail_size_bit=(code->length()-(buffer_position_->max_block_size-buffer_position_->bit_position))%BYTE_SIZE_BITS;
        }
        shift_count=code->length()-(buffer_position_->max_block_size-buffer_position_->bit_position);
        left_bits=code->bits() >> shift_count;
        length=shift_count;
        temp_buff=0;
        temp_buff |=left_bits;
        buffer_[buffer_position_->byte_position] |= temp_buff;
        ++buffer_position_->byte_position;
        buffer_position_->bit_position=0;
        if(buffer_position_->byte_position >= MAX_BUFFER_SIZE){
            fwrite(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
            for(int i=0;i<MAX_BUFFER_SIZE;i++)
                buffer_[i]=0;
            buffer_position_->byte_position=0;
        }
        while(length>=buffer_position_->max_block_size){
            shift_count-=buffer_position_->max_block_size;
            length-=buffer_position_->max_block_size;
            left_bits=(code->bits() >> shift_count) & LS_BYTE_MASK;
            temp_buff=0;
            temp_buff |= left_bits;
            buffer_[buffer_position_->byte_position] = temp_buff;
            ++buffer_position_->byte_position;
            if(buffer_position_->byte_position >= MAX_BUFFER_SIZE){
                fwrite(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
                for(int i=0;i<MAX_BUFFER_SIZE;i++)
                    buffer_[i]=0;
                buffer_position_->byte_position=0;
            }
        }
        left_bits=code->bits();
        for(int i=1;i<=length;i++){
            mask <<= 1;
            mask |= 1;
        }
        left_bits &= mask;
        left_bits <<= buffer_position_->max_block_size-length;
        temp_buff=0;
        temp_buff |=left_bits;
        buffer_[buffer_position_->byte_position] = temp_buff;
        buffer_position_->bit_position = length;
    }
}

void BufferedOutFile::Flush(){
    if(buffer_position_->bit_position != 0)
        fwrite(buffer_, sizeof(unsigned char), buffer_position_->byte_position+1, fp_);
    else{
        fwrite(buffer_, sizeof(unsigned char), buffer_position_->byte_position, fp_);
    }
    buffer_position_->bit_position=0;
    buffer_position_->byte_position=0;
}

void BufferedOutFile::PutChar(unsigned char ch){
    int shift_count;
    unsigned char left_bits, mask=0;
    if(buffer_position_->bit_position == 0){
        buffer_[buffer_position_->byte_position]=ch;
        ++buffer_position_->byte_position;
        ++size_->size_byte;
        if(buffer_position_->byte_position >= MAX_BUFFER_SIZE){
            fwrite(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
            for(int i=0;i<MAX_BUFFER_SIZE;i++)
                buffer_[i]=0;
            buffer_position_->byte_position=0;
        }
    }
    else{
        ++size_->size_byte;
        shift_count=buffer_position_->bit_position;
        left_bits=ch >> shift_count;
        buffer_[buffer_position_->byte_position] |= left_bits;
        ++buffer_position_->byte_position;
        if(buffer_position_->byte_position >= MAX_BUFFER_SIZE){
            fwrite(buffer_, sizeof(unsigned char), MAX_BUFFER_SIZE, fp_);
            for(int i=0;i<MAX_BUFFER_SIZE;i++)
                buffer_[i]=0;
            buffer_position_->byte_position=0;
        }
        left_bits=ch;
        for(int i=1;i<=shift_count;i++){
            mask <<= 1;
            mask |= 1;
        }
        left_bits &= mask;
        left_bits <<= buffer_position_->max_block_size-shift_count;
        buffer_[buffer_position_->byte_position] |= left_bits;
        buffer_position_->bit_position = shift_count;
    }
}

file_position_t BufferedOutFile::CurrentPosition()const{
    file_position_t position;
    position.byte_position=ftell(fp_)+buffer_position_->byte_position;
    position.bit_position=buffer_position_->bit_position;
    return position;
}

void BufferedOutFile::Close(){
    Flush();
    fclose(fp_);
    fp_=NULL;
}

void BufferedOutFile::Reopen(){
    fp_=fopen(os_path_.c_str(), "ab");
}
