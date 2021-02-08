#ifndef ARCHIVERITEM_H
#define ARCHIVERITEM_H
#include <vector>
#include <string>
#include "../bufferedfile/bitsizet.h"
using namespace std;


class ArchiveItem
{
public:
    ArchiveItem(const string& name);
    const string& name() const;
    bit_size_t size() const;
    void setsize(const bit_size_t& size);
    const string& archivepath() const;
    void setarchivepath(const string& path);
    void setparent(ArchiveItem* parent);
    ArchiveItem* parent() const;
    virtual ~ArchiveItem();
    void setwriten();
    bool iswriten() const;
    int itemquantity() const;
    void IncreaseQuantity(int quantity);
    void DecreaseQuantity(int quantity);
    void SetSkipOnExtract(bool skip);
    bool IsSkippedOnExtract() const;
protected:
    ArchiveItem* parent_;
    bit_size_t *size_;
    string name_;
    string archive_path_;
    bool writen_;
    int item_quantity_;
    bool skip_on_extract_;
};

#endif // ARCHIVERITEM_H
