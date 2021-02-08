#ifndef HUFFMANADDFILE_H
#define HUFFMANADDFILE_H
#include "../huffman/huffmanarchiver.h"
#include "../archiver/archivedirectory.h"
#include "../archiver/archivefile.h"
#include <QThread>


class HuffmanAddFile:public QThread
{
    Q_OBJECT
public:
    HuffmanAddFile(HuffmanArchiver *archiver, ArchiveFile *file);
    HuffmanAddFile(HuffmanArchiver *archiver, ArchiveDirectory *folder, ArchiveFile *file);
    void run();
public slots:
    void Cancell();
signals:
    void Finished();
private:
    HuffmanArchiver *archiver_;
    ArchiveDirectory *folder_;
    ArchiveFile *file_;
};

#endif // HUFFMANADDFILE_H
