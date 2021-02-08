#include "huffmanremovefolder.h"

HuffmanRemoveFolder::HuffmanRemoveFolder(HuffmanArchiver *archiver, ArchiveDirectory *dest, ArchiveDirectory *src){
    archiver_=archiver;
    dest_=dest;
    src_=src;
}

HuffmanRemoveFolder::HuffmanRemoveFolder(HuffmanArchiver *archiver, ArchiveDirectory *src){
    archiver_=archiver;
    src_=src;
    dest_=NULL;
}

void HuffmanRemoveFolder::run(){
    if(dest_==NULL)
        archiver_->RemoveFolder(src_);
    else
        archiver_->RemoveFolder(dest_, src_);
    emit Finished();
}

void HuffmanRemoveFolder::Cancell(){
    archiver_->Cancell();
}


