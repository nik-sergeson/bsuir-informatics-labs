#ifndef BUFFEREDOUTFILE_H_INCLUDED
#define BUFFEREDOUTFILE_H_INCLUDED
#include <stdio.h>
#include <string>
#include "../huffman/huffmancode.h"
#include "archiverexception.h"
#include "bufferedbitfile.h"
using namespace std;


class BufferedOutFile:public BufferedBitFile
{
public:
    BufferedOutFile(const string& os_path);
    void WriteCode(const HuffmanCode* code);
    void Flush();
    void PutChar(unsigned char ch);
    file_position_t CurrentPosition() const;
    void Close();
    void Reopen();
};
#endif // BUFFEREDOUTFILE_H_INCLUDED
