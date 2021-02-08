#include "bufferedbitfile.h"

BufferedBitFile::BufferedBitFile(const string& os_path)
{
    size_=CreateBitSize();
    buffer_position_=CreateBufferPosition(MAX_BLOCK_SIZE);
    os_path_=os_path;
    for(int i=0;i<MAX_BUFFER_SIZE;++i)
        buffer_[i]=0;
}

FILE* BufferedBitFile::fp() const{
    return fp_;
}

BufferedBitFile::~BufferedBitFile(){
    if(fp_!=NULL){
        fclose(fp_);
        fp_=NULL;
    }
    FreeBitSize(size_);
    FreeBufferPosition(buffer_position_);
}


bit_size_t BufferedBitFile::size() const{
    bit_size_t size;
    size.size_byte=size_->size_byte;
    size.tail_size_bit=size_->tail_size_bit;
    return size;
}
