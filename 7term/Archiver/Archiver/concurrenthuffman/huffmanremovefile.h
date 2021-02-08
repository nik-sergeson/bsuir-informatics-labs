#ifndef HUFFMANREMOVEFILE_H
#define HUFFMANREMOVEFILE_H
#include "../huffman/huffmanarchiver.h"
#include "../archiver/archivedirectory.h"
#include "../archiver/archivefile.h"
#include <QThread>


class HuffmanRemoveFile:public QThread
{
    Q_OBJECT
public:
    HuffmanRemoveFile(HuffmanArchiver *archiver, ArchiveFile *file);
    HuffmanRemoveFile(HuffmanArchiver *archiver, ArchiveDirectory *folder, ArchiveFile *file);
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

#endif // HUFFMANREMOVEFILE_H
