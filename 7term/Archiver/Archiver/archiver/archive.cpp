#include "archive.h"

Archive::Archive(const string& os_path)
{
    archive_root_=new ArchiveDirectory("");
    archive_root()->setparent(NULL);
    os_path_=os_path;
    item_quantity_=0;
}

void Archive::AddFile(ArchiveDirectory* destination, ArchiveFile* file){
    destination->AddFile(file);
    file->setparent(destination);
    ++item_quantity_;
}

void Archive::AddFolder(ArchiveDirectory* destination, ArchiveDirectory *folder){
    destination->AddFolder(folder);
    folder->setparent(destination);
    item_quantity_+=folder->itemquantity()+1;
}

void Archive::RemoveFile(ArchiveDirectory* folder,ArchiveFile *file){
    folder->RemoveFile(file);
    --item_quantity_;
}

Archive::~Archive(){
    delete archive_root_;
}

ArchiveDirectory* Archive::archive_root() const{
    return archive_root_;
}

const string& Archive::ospath() const{
    return os_path_;
}

void Archive::RemoveFolder(ArchiveDirectory* destination, ArchiveDirectory* folder){
    item_quantity_-=folder->itemquantity()+1;
    destination->RemoveFolder(folder);    
}

int Archive::ItemQuantity() const{
    return item_quantity_;
}
