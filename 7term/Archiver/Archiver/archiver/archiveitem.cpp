#include "archiveitem.h"

ArchiveItem::ArchiveItem(const string& name)
{
    name_=name;
    size_=CreateBitSize();
    archive_path_="";
    writen_=false;
    parent_=NULL;
    item_quantity_=0;
    skip_on_extract_=false;
}

ArchiveItem::~ArchiveItem(){
    FreeBitSize(size_);
}


const string& ArchiveItem::name() const{
    return name_;
}

bit_size_t ArchiveItem::size() const{
    return *size_;
}

void ArchiveItem::setsize(const bit_size_t& size){
    size_->tail_size_bit=size.tail_size_bit;
    size_->size_byte=size.size_byte;
}


const string& ArchiveItem::archivepath() const{
    return archive_path_;
}

void ArchiveItem::setarchivepath(const string& path){
    archive_path_=path;
}

ArchiveItem* ArchiveItem::parent() const{
    return parent_;
}

void ArchiveItem::setparent(ArchiveItem *parent){
    archive_path_="";
    parent_=parent;
    if(parent!=NULL && !parent->archivepath().empty()){
        archive_path_+=parent->archivepath()+"/";
    }
    archive_path_+=name_;
}

void ArchiveItem::setwriten(){
    writen_=true;
}

bool ArchiveItem::iswriten() const{
    return writen_;
}

void ArchiveItem::IncreaseQuantity(int quantity){
    item_quantity_+=quantity;
}

int ArchiveItem::itemquantity() const{
    return item_quantity_;
}

void ArchiveItem::DecreaseQuantity(int quantity){
    item_quantity_-=quantity;
}

void ArchiveItem::SetSkipOnExtract(bool skip){
    skip_on_extract_=skip;
}

bool ArchiveItem::IsSkippedOnExtract() const{
    return skip_on_extract_;
}
