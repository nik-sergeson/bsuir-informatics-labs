#ifndef ARCHIVEFILE_H
#define ARCHIVEFILE_H
#include "archiveitem.h"
#include <QMetaType>
#include "../fileutils/fileposition.h"

class ArchiveDirectory;

class ArchiveFile:public ArchiveItem
{
public:
    ArchiveFile(const string& os_path, const string& name);
    ArchiveFile(const string& name);
    const string& ospath() const;
    file_position_t position() const;
    void setposition(const file_position_t& position);
    ~ArchiveFile();
private:
    string os_path_;
    file_position_t *position_;
};

Q_DECLARE_METATYPE(ArchiveFile*)
#endif // ARCHIVEFILE_H
