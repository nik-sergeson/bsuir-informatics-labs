#ifndef HUFFMANADDFOLDER_H
#define HUFFMANADDFOLDER_H
#include "../huffman/huffmanarchiver.h"
#include "../archiver/archivedirectory.h"
#include "../archiver/archivefile.h"
#include <QThread>


class HuffmanAddFolder:public QThread
{
    Q_OBJECT
public:
    HuffmanAddFolder(HuffmanArchiver *archiver, ArchiveDirectory *src);
    HuffmanAddFolder(HuffmanArchiver *archiver,ArchiveDirectory *dest, ArchiveDirectory *src);
    void run();
public slots:
    void Cancell();
signals:
    void Finished();
private:
    HuffmanArchiver *archiver_;
    ArchiveDirectory *dest_;
    ArchiveDirectory *src_;
};

#endif // HUFFMANADDFOLDER_H
