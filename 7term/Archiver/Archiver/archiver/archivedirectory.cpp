#include "archivedirectory.h"

ArchiveDirectory::ArchiveDirectory(const string& name):ArchiveItem(name){
    size_->tail_size_bit=DIR_SIZE;
    size_->size_byte=DIR_SIZE;
    item_quantity_=0;
}

ArchiveDirectory::ArchiveDirectory():ArchiveItem(""){
    size_->size_byte=DIR_SIZE;
    size_->tail_size_bit=DIR_SIZE;
    item_quantity_=0;
}

const vector<ArchiveDirectory *>& ArchiveDirectory::folders() const{
    return folders_;
}

const vector<ArchiveFile *>& ArchiveDirectory::files() const{
    return files_;
}

void ArchiveDirectory::AddFile(ArchiveFile* file){
    ArchiveItem *parent=parent_;
    files_.push_back(file);
    file->setparent(this);
    ++item_quantity_;
    while (parent) {
       parent->IncreaseQuantity(1);
       parent=parent->parent();
    }
}

void ArchiveDirectory::AddFolder(ArchiveDirectory* folder){
    ArchiveItem *parent=parent_;
    folders_.push_back(folder);
    folder->setparent(this);
    item_quantity_+=folder->itemquantity()+1;
    while (parent) {
       parent->IncreaseQuantity(folder->itemquantity()+1);
       parent=parent->parent();
    }
}

void ArchiveDirectory::RemoveFolder(ArchiveDirectory* folder){
    ArchiveItem *parent=parent_;
    vector<ArchiveDirectory *>::iterator folder_it=find(folders_.begin(), folders_.end(), folder);
    if(folder_it!=folders_.end()){
        item_quantity_-=(*folder_it)->itemquantity()+1;
        while (parent) {
           parent->DecreaseQuantity((*folder_it)->itemquantity()+1);
           parent=parent->parent();
        }
        folders_.erase(folder_it);
    }
}

void ArchiveDirectory::RemoveFile(ArchiveFile* file){
    ArchiveItem *parent=parent_;
    vector<ArchiveFile *>::iterator file_it=find(files_.begin(), files_.end(), file);
    if(file_it!=files_.end()){
        --item_quantity_;
        while (parent) {
           parent->DecreaseQuantity(1);
           parent=parent->parent();
        }
        files_.erase(file_it);
    }
}

ArchiveDirectory::~ArchiveDirectory(){
    for(vector<ArchiveDirectory *>::iterator folder_it=folders_.begin(); folder_it!=folders_.end();++folder_it){
        delete *folder_it;
    }
    for(vector<ArchiveFile *>::iterator file_it=files_.begin(); file_it!=files_.end(); ++file_it){
        delete *file_it;
    }
}


vector<ArchiveFile *> ArchiveDirectory::AllFiles() const{
    vector<ArchiveDirectory *> folders=folders_, curr_folders;
    vector<ArchiveFile *> files=files_, curr_files;
    int folder_it=0;
    while(folder_it<folders.size()){
        curr_folders=folders[folder_it]->folders();
        curr_files=folders[folder_it]->files();
        folders.insert(folders.end(), curr_folders.begin(), curr_folders.end());
        files.insert(files.end(), curr_files.begin(), curr_files.end());
        ++folder_it;
    }
    return files;
}

vector<ArchiveDirectory *> ArchiveDirectory::AllFolders() const{
    vector<ArchiveDirectory *> folders=folders_, curr_folders;
    int folder_it;
    while(folder_it<folders.size()){
        curr_folders=folders[folder_it]->folders();
        folders.insert(folders.end(), curr_folders.begin(), curr_folders.end());
        ++folder_it;
    }
    return folders;
}

bool ArchiveDirectory::HasFileName(const string &file_name){
    for(vector<ArchiveFile *>::iterator file=files_.begin(); file!=files_.end();++file)
        if((*file)->name()==file_name)
            return true;
    return false;
}

bool ArchiveDirectory::HasFolderName(const string &folder_name){
    for(vector<ArchiveDirectory *>::iterator folder=folders_.begin(); folder!=folders_.end();++folder)
        if((*folder)->name()==folder_name)
            return true;
    return false;
}

