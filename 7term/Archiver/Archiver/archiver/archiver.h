#ifndef ARCHIVER_H
#define ARCHIVER_H
#include "archiveitem.h"
#include "archive.h"
using namespace std;


class Archiver
{
public:
    Archiver();
    virtual Archive* Open(const string& os_path)=0;
    virtual void Close()=0;
    virtual Archive* New(const string& os_path)=0;
    virtual void AddFile(ArchiveFile* file)=0;
    virtual void AddFolder(ArchiveDirectory *dir)=0;
    virtual void AddFile(ArchiveDirectory* destination, ArchiveFile* file)=0;
    virtual void AddFolder(ArchiveDirectory* destination, ArchiveDirectory* folder)=0;
    virtual void RemoveFile(ArchiveDirectory* destination, ArchiveFile* file)=0;
    virtual void RemoveFolder(ArchiveDirectory* destination, ArchiveDirectory* folder)=0;
    virtual void ExtractFile(ArchiveFile* file, const string& extract_path)=0;
    virtual void ExtractFolder(ArchiveDirectory* folder, const string& extract_path)=0;
    virtual bool ArchiveIsOpened()=0;
    virtual ~Archiver();
};

#endif // ARCHIVER_H
