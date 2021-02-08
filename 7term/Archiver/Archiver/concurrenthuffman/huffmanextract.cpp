#include "huffmanextract.h"

HuffmanExtract::HuffmanExtract(HuffmanArchiver *archiver, ArchiveDirectory *dir, const string& extract_path){
    archiver_=archiver;
    dir_=dir;
    file_=NULL;
    extract_path_=extract_path;
}

HuffmanExtract::HuffmanExtract(HuffmanArchiver *archiver, ArchiveFile *file, const string& extract_path){
    archiver_=archiver;
    dir_=NULL;
    file_=file;
    extract_path_=extract_path;
}

void HuffmanExtract::run(){
    if(dir_!=NULL)
        archiver_->ExtractFolder(dir_, extract_path_);
    else if(file_!=NULL)
        archiver_->ExtractFile(file_, extract_path_);
    emit Finished();
}

void HuffmanExtract::Cancell(){
    archiver_->Cancell();
}
