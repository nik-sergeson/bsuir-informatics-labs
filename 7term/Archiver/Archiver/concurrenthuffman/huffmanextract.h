#ifndef HUFFMANEXTRACT_H
#define HUFFMANEXTRACT_H
#include "../huffman/huffmanarchiver.h"
#include "../archiver/archivedirectory.h"
#include "../archiver/archivefile.h"
#include <QThread>
#include <string>
using namespace std;


class HuffmanExtract:public QThread
{
    Q_OBJECT
public:
    HuffmanExtract(HuffmanArchiver *archiver, ArchiveDirectory *dir, const string& extract_path);
    HuffmanExtract(HuffmanArchiver *archiver, ArchiveFile *file, const string& extract_path);
    void run();
public slots:
    void Cancell();
signals:
    void Finished();
private:
    HuffmanArchiver *archiver_;
    ArchiveDirectory *dir_;
    ArchiveFile *file_;
    string extract_path_;
};

#endif // HUFFMANEXTRACT_H
