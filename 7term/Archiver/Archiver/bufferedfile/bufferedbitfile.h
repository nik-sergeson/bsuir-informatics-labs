#ifndef BUFFEREDBITFILE_H
#define BUFFEREDBITFILE_H
#include <string>
#include <cstdio>
#include "bitsizet.h"
#include "bufferposition.h"
#include "../fileutils/fileposition.h"
using namespace std;

#define MAX_BUFFER_SIZE 1000000
#define MAX_BLOCK_SIZE 8
#define MSB_MASK 0x80

class BufferedBitFile
{
public:
    BufferedBitFile(const string& os_path);
    FILE* fp() const;
    bit_size_t size() const;
    virtual file_position_t CurrentPosition() const=0;
    virtual ~BufferedBitFile();
protected:
    buffer_position_t *buffer_position_;
    unsigned char buffer_[MAX_BUFFER_SIZE];
    FILE *fp_;
    bit_size_t *size_;
    string os_path_;
};

#endif // BUFFEREDBITFILE_H
