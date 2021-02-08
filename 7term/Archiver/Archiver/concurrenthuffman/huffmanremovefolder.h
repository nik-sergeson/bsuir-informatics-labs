#ifndef HUFFMANREMOVEFOLDER_H
#define HUFFMANREMOVEFOLDER_H
#include "../huffman/huffmanarchiver.h"
#include "../archiver/archivedirectory.h"
#include "../archiver/archivefile.h"
#include <QThread>


class HuffmanRemoveFolder:public QThread
{
    Q_OBJECT
public:
    HuffmanRemoveFolder(HuffmanArchiver *archiver, ArchiveDirectory *src);
    HuffmanRemoveFolder(HuffmanArchiver *archiver,ArchiveDirectory *dest, ArchiveDirectory *src);
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

#endif // HUFFMANREMOVEFOLDER_H
