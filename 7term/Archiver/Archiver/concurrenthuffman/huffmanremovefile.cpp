#include "huffmanremovefile.h"

HuffmanRemoveFile::HuffmanRemoveFile(HuffmanArchiver *archiver, ArchiveDirectory *folder, ArchiveFile *file){
    archiver_=archiver;
    folder_=folder;
    file_=file;
}

HuffmanRemoveFile::HuffmanRemoveFile(HuffmanArchiver *archiver, ArchiveFile *file){
    archiver_=archiver;
    file_=file;
    folder_=NULL;
}

void HuffmanRemoveFile::run(){
    if(folder_==NULL)
        archiver_->RemoveFile(file_);
    else
        archiver_->RemoveFile(folder_, file_);
    emit Finished();
}

void HuffmanRemoveFile::Cancell(){
    archiver_->Cancell();
}

