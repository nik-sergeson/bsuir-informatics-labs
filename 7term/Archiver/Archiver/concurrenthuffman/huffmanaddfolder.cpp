#include "huffmanaddfolder.h"

HuffmanAddFolder::HuffmanAddFolder(HuffmanArchiver *archiver, ArchiveDirectory *dest, ArchiveDirectory *src){
    archiver_=archiver;
    dest_=dest;
    src_=src;
}

HuffmanAddFolder::HuffmanAddFolder(HuffmanArchiver *archiver, ArchiveDirectory *src){
    archiver_=archiver;
    src_=src;
    dest_=NULL;
}

void HuffmanAddFolder::run(){
    if(dest_==NULL)
        archiver_->AddFolder(src_);
    else
        archiver_->AddFolder(dest_, src_);
    emit Finished();
}

void HuffmanAddFolder::Cancell(){
    archiver_->Cancell();
}
