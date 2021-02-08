#ifndef ARCHIVEDIRECTORY_H
#define ARCHIVEDIRECTORY_H
#include <QMetaType>
#include <algorithm>
#include "archiveitem.h"
#include "archivefile.h"

#define DIR_SIZE -1

class ArchiveDirectory:public ArchiveItem
{
public:
    ArchiveDirectory();
    ArchiveDirectory(const string& name);
    const vector<ArchiveDirectory *>& folders() const;
    const vector<ArchiveFile *>& files() const;
    vector<ArchiveFile *> AllFiles() const;
    vector<ArchiveDirectory *> AllFolders() const;
    void AddFile(ArchiveFile* file);
    void AddFolder(ArchiveDirectory* folder);
    void RemoveFolder(ArchiveDirectory* folder);
    void RemoveFile(ArchiveFile* file);
    bool HasFileName(const string& file_name);
    bool HasFolderName(const string& folder_name);
    ~ArchiveDirectory();
private:
    vector<ArchiveFile *> files_;
    vector<ArchiveDirectory *> folders_;
};

Q_DECLARE_METATYPE(ArchiveDirectory*)
#endif // ARCHIVEDIRECTORY_H
