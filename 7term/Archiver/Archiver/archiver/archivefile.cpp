#include "archivefile.h"
#include "archivedirectory.h"

ArchiveFile::ArchiveFile(const string& os_path, const string& name):ArchiveItem(name){
    os_path_=os_path;
    position_=CreateFilePosition();
}

ArchiveFile::ArchiveFile(const string &name):ArchiveItem(name){
    position_=CreateFilePosition();
}

const string& ArchiveFile::ospath() const{
    return os_path_;
}

file_position_t ArchiveFile::position() const{
    return *position_;
}

void ArchiveFile::setposition(const file_position_t& position){
    position_->bit_position=position.bit_position;
    position_->byte_position=position.byte_position;
}

ArchiveFile::~ArchiveFile(){
    FreeFilePosition(position_);
}
