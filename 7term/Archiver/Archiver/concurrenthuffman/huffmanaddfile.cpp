#include "huffmanaddfile.h"

HuffmanAddFile::HuffmanAddFile(HuffmanArchiver *archiver, ArchiveDirectory *folder, ArchiveFile *file){
    archiver_=archiver;
    folder_=folder;
    file_=file;
}

HuffmanAddFile::HuffmanAddFile(HuffmanArchiver *archiver, ArchiveFile *file){
    archiver_=archiver;
    file_=file;
    folder_=NULL;
}

void HuffmanAddFile::run(){
    if(folder_==NULL)
        archiver_->AddFile(file_);
    else
        archiver_->AddFile(folder_, file_);
    emit Finished();
}

void HuffmanAddFile::Cancell(){
    archiver_->Cancell();
}

