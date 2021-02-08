#ifndef BUFFEREDINFILE_H_INCLUDED
#define BUFFEREDINFILE_H_INCLUDED
#include <stdio.h>
#include <string>
#include "bufferedbitfile.h"
#include "bitsizet.h"
#include "archiverexception.h"
#include "../fileutils/fileposition.h"
using namespace std;


class BufferedInFile:public BufferedBitFile
{
public:
    BufferedInFile(const string& path);
    int GetBit();
    int GetByte();
    void ReadBlock(const bit_size_t& size, const file_position_t& position);
    void ReadBlock();
    void Close();
    void Reopen();
    file_position_t CurrentPosition() const;
private:
    file_position_t buffer_start_position;
};
#endif // BUFFEREDINFILE_H_INCLUDED
