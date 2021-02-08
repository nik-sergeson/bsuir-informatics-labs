#ifndef ARCHIVE_H
#define ARCHIVE_H
#include <algorithm>
#include "archiveitem.h"
#include "archivefile.h"
#include "archivedirectory.h"
using namespace std;


class Archive
{
public:
    Archive(const string& os_path);
    void AddFile(ArchiveDirectory* destination, ArchiveFile* file);
    void AddFolder(ArchiveDirectory* destination, ArchiveDirectory* folder);
    void RemoveFile(ArchiveDirectory* folder,ArchiveFile* file);
    void RemoveFolder(ArchiveDirectory* destination, ArchiveDirectory* folder);
    const string& ospath() const;
    int ItemQuantity() const;
    ArchiveDirectory* archive_root() const;
    ~Archive();
private:
    string os_path_;
    int item_quantity_;
    ArchiveDirectory* archive_root_;
};

#endif // ARCHIVE_H
